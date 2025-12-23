from .ai import generate_places_from_prompt, map_place_names_to_places

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Package
from .serializers import PackageCreateSerializer
from places.models import Place

from django.shortcuts import get_object_or_404
from recommends.models import AIRecommendLog
from places.serializers import PlaceSerializer


class PackageGenerateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PackageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        package = serializer.save(user=request.user)

        place_names = generate_places_from_prompt(package.prompt)
        places = map_place_names_to_places(place_names)

        # fallback (GPT 결과가 비었을 때)
        if not places:
            places = Place.objects.all()[:5]

        return Response(
            {
                "package_id": package.id,
                "recommended_place_ids": [p.id for p in places]
            },
            status=status.HTTP_201_CREATED
        )


class PackageDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, package_id):
        package = get_object_or_404(
            Package,
            id=package_id,
            user=request.user
        )

        # 지금은 mock: 최근 추천된 장소
        places = Place.objects.all()[:5]

        # AI 추천 노출 로그 저장 (여기가 핵심)
        logs = []
        for place in places:
            logs.append(
                AIRecommendLog(
                    user=request.user,
                    place=place,
                    package=package
                )
            )
        AIRecommendLog.objects.bulk_create(logs)

        return Response({
            "package": {
                "id": package.id,
                "prompt": package.prompt
            },
            "places": PlaceSerializer(places, many=True).data
        })
