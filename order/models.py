from django.db import models


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='사용자')
# 유저앱 안에 있는 models.py에 유저클래스를 넣어주겟다.
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)
# 주문도 문자열로 잘표현하기 위해서 이렇게 한거임

    class Meta:
        db_table = 'ryu_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
# _plural 붙은거는 복수형 지정하기위해
# 어드민에서 쓰기 편하게 클래스 안에 메타 클래스를 선언해준다.
#
