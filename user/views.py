from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView  # 폼뷰를 가져온다
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import User


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'  # url용으로 만듬
    form_class = RegisterForm  # 레지스터폼클래스를 참조해라
    success_url = '/'  # 성공시 이동

    def form_valid(self, form):
        user = User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()

        return super().form_valid(form)
    # 유효성은 forms.py에서 저장은 views.py에서 form_vaild 내장함수로
    # 유효성 검사가 끝나면 저장하는것도 실행이 된다 .
    # 계정만들시 기본 레벨을 유저로 해주고


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):  # 유효성 검사  고인이 정상적으로 끝났을때 세션에 저장함
        self.request.session['user'] = form.data.get(
            'email')  # 로그인한 사용자의 이메일정보
        return super().form_valid(form)  # 기존의 폼valid 함수를 호출
        # form에서   else:   self.email = user.email 이렇게 할필요없이
        # 직접 form.data.get('')할수 있다


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')
