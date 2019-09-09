from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView  # 폼뷰를 가져온다
from .models import Product
from .forms import RegisterForm


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
# 포문에 기본 변수가 오브젝트리스트, 싫으면  views에서 context_object_name 설정해야함


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'
