# users/urls.py
from django.urls import path, include
from .views import user_login, user_logout, UserViewSet, register_api, login_api, test_api, current_user, check_login_api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/', include(router.urls)),  # /users/api/list/ 로 접근 가능
    path('register/', register_api),
    path('login_api/', login_api),
    path('ping/', test_api),  # /users/ping/
    path('me/', current_user), #현재 로그인된 사용자 정보 확인
    path('check/', check_login_api),

]
