from django.contrib import admin
from django.urls import path, include
from apps.users import views as user_views
from django.conf import settings                     # ✅ 추가
from django.conf.urls.static import static           # ✅ 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('', user_views.user_login, name='home'),
    path('api/', include('apps.books.urls')),
    path('api/accounts/', include('apps.accounts.urls')),
    path('users/', include('apps.users.urls')),
]

# ✅ 여기를 꼭 추가해줘야 static 파일(css/js) 적용됨
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
