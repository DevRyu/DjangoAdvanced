from django.shortcuts import render
from django.views.generic import ListView, DetailView  # 디테일뷰를 사용한다.
from django.views.generic.edit import FormView  # 폼뷰를 가져온다
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
# 포문에 기본 변수가 오브젝트리스트, 싫으면  views에서 context_object_name 설정해야함


class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    # 쿼리셋을 지정해서 필터를사용하면 조건에 맞는 프로젝트들만 가져오지만 전체다가져올거임.
    queryset = Product.objects.all()
    context_object_name = 'product'  # 변수명을 지정가능함

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # order\forms.py 폼을 생성할때 리퀘스를 전달해줌
        context['form'] = OrderForm(self.request)
        return context
        # 주문버튼을 누르면 데이터를 받아서  context에 넘겨주는 함수
