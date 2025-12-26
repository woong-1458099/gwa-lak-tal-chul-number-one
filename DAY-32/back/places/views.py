from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Place
from .serializers import PlaceSerializer
from recommends.models import SearchLog
import math


class PlaceSearchAPIView(APIView):
    def get(self, request):
        queryset = Place.objects.all()

        keyword = request.query_params.get('keyword')
        min_rating = request.query_params.get('min_rating')
        center_lat = request.query_params.get('center_lat')
        center_lng = request.query_params.get('center_lng')
        radius = request.query_params.get('radius')

        # 키워드 필터
        if keyword:
            queryset = queryset.filter(name__icontains=keyword)

        # 평점 필터 (DB에서)
        if min_rating:
            queryset = queryset.filter(rating__gte=float(min_rating))

        # 거리 필터 (Python에서)
        if center_lat and center_lng and radius:
            center_lat = float(center_lat)
            center_lng = float(center_lng)
            radius = float(radius)

            filtered = []
            for place in queryset:
                distance = self._distance(
                    center_lat, center_lng,
                    place.lat, place.lng
                )
                if distance <= radius:
                    filtered.append(place)

            queryset = filtered

        # 검색 로그 저장
        SearchLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            keyword=keyword or '',
            center_lat=center_lat if center_lat else None,
            center_lng=center_lng if center_lng else None,
        )

        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data)

    def _distance(self, lat1, lng1, lat2, lng2):
        # 위도/경도 간단 거리 계산 (km)
        return math.sqrt((lat1 - lat2)**2 + (lng1 - lng2)**2) * 111
