from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework import viewsets
from .serializers import UserSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def ping(request):
    return JsonResponse({'message': 'pong'}, status=200)

@csrf_exempt
def test_api(request):
    return JsonResponse({'message': 'API 연결 성공!'}, status=200)

@csrf_exempt
def register_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            is_admin = data.get("is_admin", False)

            if not username or not password:
                return JsonResponse({'error': '아이디와 비밀번호를 모두 입력하세요.'}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': '이미 존재하는 아이디입니다.'}, status=409)

            user = User.objects.create_user(username=username, password=password)
            if is_admin:
                user.is_staff = True
            user.save()
            return JsonResponse({'message': '회원가입이 완료되었습니다!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 JSON 형식입니다.'}, status=400)

    return JsonResponse({'message': '회원가입 API입니다.'})

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # ✅ 세션 연결 필수
                return JsonResponse({'message': '로그인 성공!', 'is_admin': user.is_staff}, status=200)
            else:
                return JsonResponse({'error': '아이디 또는 비밀번호가 올바르지 않습니다.'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 JSON 형식입니다.'}, status=400)

    return JsonResponse({'message': '로그인 API입니다.'}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def current_user(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'username': request.user.username,
            'is_admin': request.user.is_staff
        })
    else:
        return JsonResponse({'error': '로그인되지 않았습니다.'}, status=401)

@csrf_exempt
def check_login_api(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'is_authenticated': True,
            'username': request.user.username,
            'is_admin': request.user.is_staff,
        })
    return JsonResponse({'is_authenticated': False})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "로그인 정보가 올바르지 않습니다.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
