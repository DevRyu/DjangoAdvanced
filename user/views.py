from django.shortcuts import render
from django.views.generic.edit import FormView  # 폼뷰를 가져온다
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'  # url용으로 만듬
    form_class = RegisterForm  # 레지스터폼클래스를 참조해라
    success_url = '/'  # 성공시 이동


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):  # 유효성 검사  고인이 정상적으로 끝났을때 세션에 저장함
        self.request.session['user'] = form.email  # 로그인한 사용자의 이메일정보
        return super().form_valid(form)  # 기존의 폼valid 함수를 호출
