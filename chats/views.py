from rest_framework import viewsets, permissions
from .models import Chat
from .serializers import ChatSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all().order_by('-timestamp')  # 최신순 정렬
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)  # 예시: sender를 로그인 유저로 설정
