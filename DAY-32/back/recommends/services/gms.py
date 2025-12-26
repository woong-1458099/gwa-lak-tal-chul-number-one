import requests
from django.conf import settings

GMS_URL = "https://gms.ssafy.io/gmsapi/api.openai.com/v1/chat/completions"

def call_gms_chat(prompt: str) -> str:
    if not settings.GMS_KEY:
        raise RuntimeError("GMS_KEY가 설정되지 않았습니다. back/.env 확인")

    payload = {
        "model": getattr(settings, "GMS_MODEL", "gpt-4.1-nano"),
        "messages": [
            {"role": "system", "content": "Answer in Korean. You are a travel planner."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 800,
    }

    res = requests.post(
        GMS_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.GMS_KEY}",
        },
        json=payload,
        timeout=30,
    )

    if res.status_code >= 400:
        raise RuntimeError(f"GMS 호출 실패({res.status_code}): {res.text}")

    data = res.json()
    return data["choices"][0]["message"]["content"]
