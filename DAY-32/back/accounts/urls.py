from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    SignupAPIView, 
    TestAuthAPIView,
    UserPreferenceAPIView,
    )

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),      # 로그인
    path('token/refresh/', TokenRefreshView.as_view()), # 토큰 갱신
    path('test/', TestAuthAPIView.as_view()),
    path('preferences/', UserPreferenceAPIView.as_view()),
]
