from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name
# 어드민에서 문자열을 반환해줘야 http://127.0.0.1:8000/admin/order/order/ 에서 이름 잘나옴

    class Meta:
        db_table = 'ryu_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
# _plural 붙은거는 복수형 지정하기위해
