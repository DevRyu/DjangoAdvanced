from django.shortcuts import redirect
from .models import User


def login_required(function):
    def wrap(request, *args, **kwargs):
        # 래핑할 함수와 기존의 dispatch함수의 인자를 맞추어줘야함
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        # 로그인상태가 아니거나 유저가 아니면 로그인뷰로 리다이렉트
        return function(request, *args, **kwargs)
    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        # 래핑할 함수와 기존의 dispatch함수의 인자를 맞추어줘야함
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        # 로그인상태가 아니거나 유저가 아니면 로그인뷰로 리다이렉트
        user = User.objects.get(email=user)
        # from .model import User 유저 클래스를 가져오고
        if user.level != 'admin':
            return redirect('/')
        # 어드민 유저 레벨이 아니면 홈으로 보내라
        return function(request, *args, **kwargs)
    return wrap
