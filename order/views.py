from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.db import transaction
from user.decorators import login_required
from product.models import Product
from user.models import User
from .forms import RegisterForm
from .models import Order


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    # 템플릿네임은 필요가 없음 상품 상세보기에 있기때문에
    form_class = RegisterForm
    success_url = '/product/'
    # 클래스 뷰안에 kwargs 폼 뷰생성시 어떤 인자값을 전달할것인지 알려줌

    def form_valid(self, form):
        with transaction.atomic():
            # 트렌젝션 어토믹 함수 사용할거임(전체 성공시 성공,하나라도 실패시 실패)
            prod = Product.objects.get(pk=form.data.get('product'))
            # prod를 불러오고
            order = Order(
                quantity=form.data.get('quantity'),
                product=prod,
                user=User.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            # 주문이 끝나면 개수가 한개줄고
            prod.save()
            # 저장        # 값이 들어온지 개수, 프로덕트(pk=id일때), 유저(이메일이 유저인경우)
    # 세션의 이메일이 있으니까 확인하고  확인하고 저장
        return super().form_valid(form)

    def form_invalid(self, form):
        # TypeError at /order/create/
        return redirect('/product/' + str(form.data.get('product')))
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


@method_decorator(login_required, name='dispatch')
# 원래 클래스 뷰에서 호출할때 def dispatch라는 함수가 있음,
# 데코레이터를 밑의 클래스내에 지정할수도 있지만 메서드데코레이터로 지정하는게 편하다
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            user__email=self.request.session.get('user'))
        return queryset
    # 뷰에서 오더를 모델에 지정해서했는데
    # 로그인한 사용자만 보는게아니라 모든 사용자의 주문정보를
    # 쿼리셋에 아이디를 부여해 본인아이디에 대해서 등록된 웹을 보게 한다.
