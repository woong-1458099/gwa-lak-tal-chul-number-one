from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import SignupSerializer, UserPreferenceSerializer

from rest_framework.permissions import IsAuthenticated
from .models import UserPreference



class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "회원가입 성공"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestAuthAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"{request.user.username} 로그인 상태입니다."
        })
    

class UserPreferenceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        preference, _ = UserPreference.objects.get_or_create(
            user=request.user
        )
        serializer = UserPreferenceSerializer(preference)
        return Response(serializer.data)

    def post(self, request):
        preference, _ = UserPreference.objects.get_or_create(
            user=request.user
        )
        serializer = UserPreferenceSerializer(
            preference,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

