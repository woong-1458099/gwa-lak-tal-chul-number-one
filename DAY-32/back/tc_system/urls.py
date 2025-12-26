from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def ping(request):
    return JsonResponse({"ok": True})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/ping/", ping),

    # ✅ 추천 AI endpoint
    path("api/ai/", include("recommends.urls")),

    path("api/accounts/", include("accounts.urls")),
    path("api/places/", include("places.urls")),
    path("api/recommends/", include("recommends.urls")),  # 있어도 되고 없어도 됨(중복 include OK)
]
