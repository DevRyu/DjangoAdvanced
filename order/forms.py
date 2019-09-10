from django import forms
from .models import Order
from product.models import Product
from user.models import User
from django.db import transaction


class RegisterForm(forms.Form):
    # 리퀘스트에 직접적으로 폼에 전달할수 없으므로 생성자 함수에서 폼뷰 쓸거임
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 상속받음
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품설명', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        # print(self.request.session)
        # 위를 프린트해보면 세션에 접근할수 있다.
        # 유저는 세션에서 가져온다.

        if quantity and product and user:
            with transaction.atomic():
                # 트렌젝션 어토믹 함수 사용할거임(전체 성공시 성공,하나라도 실패시 실패)
                prod = Product.objects.get(pk=product)
                # prod를 불러오고
                order = Order(
                    quantity=quantity,
                    product=prod,
                    user=User.objects.get(email=user)
                )
                order.save()
                prod.stock -= quantity
                # 주문이 끝나면 개수가 한개줄고
                prod.save()
                # 저장        # 값이 들어온지 개수, 프로덕트(pk=id일때), 유저(이메일이 유저인경우)
        # 세션의 이메일이 있으니까 확인하고  확인하고 저장
        else:  # 값이 없을때 에러 발생
            self.product = product
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
