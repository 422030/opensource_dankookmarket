from django.urls import path, include
from .views import (
    user_login, user_logout, UserViewSet,
    register_api, login_api, ping, current_user, check_login_api
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/', include(router.urls)),
    path('register/', register_api),
    path('login_api/', login_api),  # ✅ 로그인 API 주소
    path('ping/', ping),
    path('me/', current_user),
    path('check/', check_login_api),
]
