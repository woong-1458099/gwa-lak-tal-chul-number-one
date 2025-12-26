from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from places.models import Place
from packages.models import Package
from places.serializers import PlaceSerializer
from .models import PlaceClickLog, AIRecommendLog
from .utils import calculate_place_score

from .services.gms import call_gms_chat


class PlaceClickAPIView(APIView):
    def post(self, request):
        place_id = request.data.get("place_id")
        source = request.data.get("source")

        if not place_id or not source:
            return Response({"error": "place_id와 source는 필수입니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            place = Place.objects.get(id=place_id)
        except Place.DoesNotExist:
            return Response({"error": "존재하지 않는 장소입니다."}, status=status.HTTP_404_NOT_FOUND)

        PlaceClickLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            place=place,
            source=source
        )
        return Response({"message": "클릭 로그 저장 완료"}, status=status.HTTP_201_CREATED)


class AIRecommendLogAPIView(APIView):
    def post(self, request):
        package_id = request.data.get("package_id")
        place_ids = request.data.get("place_ids")

        if not package_id or not place_ids:
            return Response({"error": "package_id와 place_ids는 필수입니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            package = Package.objects.get(id=package_id)
        except Package.DoesNotExist:
            return Response({"error": "존재하지 않는 패키지입니다."}, status=status.HTTP_404_NOT_FOUND)

        places = Place.objects.filter(id__in=place_ids)

        logs = [
            AIRecommendLog(
                user=request.user if request.user.is_authenticated else None,
                place=place,
                package=package
            )
            for place in places
        ]
        AIRecommendLog.objects.bulk_create(logs)

        return Response({"message": "AI 추천 노출 로그 저장 완료"}, status=status.HTTP_201_CREATED)


class TopRecommendAPIView(APIView):
    def get(self, request):
        limit = int(request.query_params.get("limit", 10))
        places = Place.objects.all()

        scored_places = [(p, calculate_place_score(p)) for p in places]
        scored_places.sort(key=lambda x: x[1], reverse=True)

        top_places = [place for place, _score in scored_places[:limit]]
        serializer = PlaceSerializer(top_places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def ai_recommend(request):
    """
    POST /api/ai/recommend/
    """
    prompt = (request.data.get("prompt") or "").strip()
    rec_type = request.data.get("type") or "prompt"

    if not prompt:
        return Response({"error": "prompt는 필수입니다."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        text = call_gms_chat(prompt)
        return Response(
            {"type": rec_type, "prompt": prompt, "resultText": text},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"error": "추천 생성 실패", "detail": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
