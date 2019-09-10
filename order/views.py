from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm


class OrderCreate(FormView):
    # 템플릿네임은 필요가 없음 상품 상세보기에 있기때문에
    form_class = RegisterForm
    success_url = '/product/'
    # 클래스 뷰안에 kwargs 폼 뷰생성시 어떤 인자값을 전달할것인지 알려줌

    def form_invalid(self, form):
        # TypeError at /order/create/
        return redirect('/product/' + str(form.product))
        # can only concatenate str (not "int") to str 숫자형이여서 문자형으로 변환

    # 주문하기 페이지 따로 만들지 않기 때문에 템플릿네임이 지정안되서 에러발생
    # 실패 했을경우 상품 상세 페이지로 이동하는 함수를 만들어 줘야한다

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
        # 인자 값들이랑 리퀘스트값을 업데이트 해서 폼클래스를 만들겟다
