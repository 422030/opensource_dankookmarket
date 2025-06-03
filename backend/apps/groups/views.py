# apps/groups/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import GroupBuyRequest
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_group_buy(request):
    title = request.data.get('title')
    description = request.data.get('description', '')

    if not title :
        return Response({'error': '항목을 모두 입력하세요.'}, status=400)
    
    group_buy = GroupBuyRequest.objects.create(
        title=title,
        description=description,
        requester=request.user,
        status='모집 중')
    return Response({'message': '공동 구매 등록이 완료되었습니다.', 'id': group_buy.id})
