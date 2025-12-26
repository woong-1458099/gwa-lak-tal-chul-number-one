from django.urls import path
from .views import PlaceClickAPIView, AIRecommendLogAPIView, TopRecommendAPIView, ai_recommend

urlpatterns = [
    path("click/", PlaceClickAPIView.as_view()),
    path("ai-log/", AIRecommendLogAPIView.as_view()),
    path("top/", TopRecommendAPIView.as_view()),

    # ✅ 프론트가 부르는 핵심
    path("recommend/", ai_recommend, name="ai_recommend"),
]
