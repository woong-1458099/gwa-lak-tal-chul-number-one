import re
from typing import List

from django.conf import settings
from openai import OpenAI
from places.models import Place


# ✅ GMS(OpenAI 호환) 프록시 base url
# curl에서: https://gms.ssafy.io/gmsapi/api.openai.com/v1/chat/completions
GMS_BASE_URL_DEFAULT = "https://gms.ssafy.io/gmsapi/api.openai.com/v1"


def _get_client() -> OpenAI:
    """
    GMS 프록시로 OpenAI-python 클라이언트를 생성한다.
    - settings.GMS_KEY 가 있으면 그걸 사용
    - (혹시) settings.OPENAI_API_KEY 가 있으면 그걸 사용
    - base_url은 GMS 프록시로 고정
    """
    api_key = getattr(settings, "GMS_KEY", None) or getattr(settings, "OPENAI_API_KEY", None)
    if not api_key:
        raise RuntimeError("GMS_KEY 또는 OPENAI_API_KEY가 설정되지 않았습니다. (.env / settings 확인)")

    base_url = getattr(settings, "GMS_BASE_URL", None) or GMS_BASE_URL_DEFAULT
    return OpenAI(api_key=api_key, base_url=base_url)


def generate_places_from_prompt(prompt: str, top_n: int = 5) -> List[str]:
    """
    프롬프트를 기반으로 '장소 이름 리스트'만 반환한다.
    (설명/이유/시간표 없이 이름만)
    """
    prompt = (prompt or "").strip()
    if not prompt:
        return []

    model = getattr(settings, "GMS_MODEL", "gpt-4.1-nano")  # 너가 GMS에서 쓰던 모델로
    client = _get_client()

    system_msg = """
너는 실제 여행 가이드이자 일정 플래너다.
사용자는 하루 동안 현실적으로 이동 가능한 여행 코스를 원한다.

규칙:
1) 모든 추천 장소는 반드시 같은 도시 또는 같은 권역에 있어야 한다.
2) 하루 일정 기준으로 이동이 가능한 동선만 추천한다.
3) 서로 1시간 이상 이동이 필요한 장소는 절대 함께 추천하지 않는다.
4) 사용자가 특정 도시를 언급하면, 해당 도시 내부 장소만 추천한다.
5) 추천 장소는 이동 흐름을 고려해 자연스러운 순서로 나열한다. (아침 → 점심 → 오후 → 저녁 → 야경)
6) 여행 테마가 주어지면 반드시 반영한다. (힐링, 먹방, 바다, 자연, 혼행, 커플, 가족 등)
7) 관광지/휴식/산책이 균형 있게 섞이게 한다.
8) 장소 이름만 리스트로 답한다. 설명/부연/이모지/시간/이유는 절대 포함하지 않는다.
"""

    user_msg = f"""
아래 형식처럼 '장소 이름만' 리스트로 출력해.

입력: 서울에서 하루 동안 힐링 여행
출력:
- 북촌 한옥마을
- 경복궁
- 인사동
- 청계천
- 남산공원

실제 요청:
{prompt}
"""

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.55,
            max_tokens=300,
        )

        content = (resp.choices[0].message.content or "").strip()
        if not content:
            return []

        # ✅ 줄 단위 파싱: "-", "•", "1.", "1)" 등 제거
        names: List[str] = []
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue

            # 앞의 bullet/number 제거
            line = re.sub(r"^\s*[-•*]+\s*", "", line)
            line = re.sub(r"^\s*\d+[\.\)\-]\s*", "", line)

            # 혹시 따옴표/백틱 제거
            line = line.strip(" \"'`")

            if line:
                names.append(line)

        # ✅ 중복 제거(순서 유지) + top_n 제한
        uniq = []
        seen = set()
        for n in names:
            key = re.sub(r"\s+", "", n)
            if key in seen:
                continue
            seen.add(key)
            uniq.append(n)
            if len(uniq) >= top_n:
                break

        return uniq

    except Exception as e:
        # 실패 시 서버 안정성 위해 빈 리스트 반환
        print("GMS(OpenAI 호환) 호출 실패:", e)
        return []


def map_place_names_to_places(place_names: List[str]) -> List[Place]:
    """
    GPT가 준 장소 이름 리스트 -> DB Place 매핑
    - icontains 우선
    - 없으면 공백 제거 비교로 한번 더 시도
    """
    places: List[Place] = []
    for name in (place_names or []):
        name = (name or "").strip()
        if not name:
            continue

        # 1) 가장 단순한 매칭
        place = Place.objects.filter(name__icontains=name).first()

        # 2) 공백 제거해서 재시도 (ex: "해운대해수욕장" vs "해운대 해수욕장")
        if not place:
            compact = re.sub(r"\s+", "", name)
            place = Place.objects.filter(name__iregex=compact).first()

        if place:
            places.append(place)

    return places
