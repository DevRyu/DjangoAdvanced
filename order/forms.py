from django import forms
from .models import Order
from product.models import Product
from user.models import User


class RegisterForm(forms.Form):
    # 리퀘스트에 직접적으로 폼에 전달할수 없으므로 생성자 함수에서 폼뷰 쓸거임
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 상속받음
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품정보를 입력해주세요'
        },
        label='상품', widget=forms.HiddenInput  # 사용자에게 보여지지 않게
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
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product),
                user=User.objects.get(email=user)
            )
            order.save()
        # 값이 들어온지 개수, 프로덕트(pk=id일때), 유저(이메일이 유저인경우)
        # 세션의 이메일이 있으니까 확인하고  확인하고 저장
        else:  # 값이 없을때 에러 발생
            self.product = product
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
