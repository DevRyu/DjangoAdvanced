from django.shortcuts import render
from django.views.generic import ListView, DetailView  # 디테일뷰를 사용한다.
from django.views.generic.edit import FormView  # 폼뷰를 가져온다
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins


from user.decorators import admin_required
from .models import Product
from .forms import RegisterForm
from .serializers import ProductSerializer
from order.forms import RegisterForm as OrderForm


class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer
    # 시리얼라이저와 쿼리셋을 지정해서 만듬

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    # 오버라이딩해서 쿼리셋 지정
    # 모든 오브젝트를 프로덕트 받음

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

        # 제너릭API뷰로로 프로덕트리스트를 만들었다.
        # 믹스인은 컴포넌트, 겟에서는 리스트API 와 포스트에서는 생성API를 만들고 싶다면?
        # 믹스인안에 내장함수있음


class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    # RetrieveModelMixin 상세보기를 위한 믹스인

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    # 오버라이딩해서 쿼리셋 지정
    # 모든 오브젝트를 프로덕트 받음
    # url에서 pk값을 연결해줘야 (겟쿼리셋의 id와 같은) 에러가 안남

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # 믹스인안에 개발이 다되어 있어 get요청이 왓을때 mixin이 만들어준함수를 호출해주기만 하면 된다.


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
