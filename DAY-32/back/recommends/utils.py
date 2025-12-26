from django.db.models import Count
from places.models import Place
from recommends.models import PlaceClickLog, AIRecommendLog


def calculate_place_score(place):
    """
    하나의 Place에 대한 추천 점수를 계산한다.
    """

    score = 0

    # 구글 평점 점수 (기본 신뢰도)
    if place.rating:
        score += place.rating * 10  # 가중치 10

    # 클릭 점수
    click_count = PlaceClickLog.objects.filter(place=place).count()
    score += click_count * 5  # 클릭 1회당 5점

    # AI 추천 노출 점수
    ai_count = AIRecommendLog.objects.filter(place=place).count()
    score += ai_count * 3  # AI 추천 1회당 3점

    return score
