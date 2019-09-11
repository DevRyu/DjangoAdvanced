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

        # print(self.request.session)
        # 위를 프린트해보면 세션에 접근할수 있다.
        # 유저는 세션에서 가져온다.

        if not(quantity and product):
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
        # 유효성만 검사하고 없으면 에러코드 발생시킨다.
