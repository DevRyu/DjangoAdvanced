from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # 필드를 지정하지 않고 만들면 자동으로 모든필드를 가져온다
    # 시리얼라이저를 모델에 연결한다.
    class Meta:
        model = Product
        fields = '__all__'
