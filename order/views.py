from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm


class OrderCreate(FormView):
    # 템플릿네임은 필요가 없음 상품 상세보기에 있기때문에
    form_class = RegisterForm
    success_url = '/product/'
