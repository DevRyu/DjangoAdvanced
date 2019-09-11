from django.shortcuts import render
from django.views.generic import ListView, DetailView  # 디테일뷰를 사용한다.
from django.views.generic.edit import FormView  # 폼뷰를 가져온다
from django.utils.decorators import method_decorator
from user.decorators import admin_required
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
# 포문에 기본 변수가 오브젝트리스트, 싫으면  views에서 context_object_name 설정해야함


@method_decorator(admin_required, name='dispatch')
# 상품등록은 어드민데코레이터를 통해서만!
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)
        # 오버라이딩햇기 떄문에부모함수 호출


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
