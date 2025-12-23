from django.urls import path
from .views import PackageGenerateAPIView, PackageDetailAPIView

urlpatterns = [
    path('generate/', PackageGenerateAPIView.as_view()),
    path('<int:package_id>/', PackageDetailAPIView.as_view()),
]
