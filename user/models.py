from django.db import models
# Create your models here.


class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email
# 어드민에서 문자열을 반환해줘야 http://127.0.0.1:8000/admin/order/order/ 에서 이메일 잘나옴

    class Meta:
        db_table = 'ryu_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
# _plural 붙은거는 복수형 지정하기위해
