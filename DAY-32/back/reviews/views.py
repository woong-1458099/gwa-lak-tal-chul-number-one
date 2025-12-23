from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def list_by_place(request, place_id):
    return Response([])

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, place_id):
    return Response({'message': 'review created', 'place_id': place_id}, status=status.HTTP_201_CREATED)
