from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
# 콤마를 안쓰면 튜플로 인식 못하므로 주의하자!
# 모델에 foreign키이니까?


admin.site.register(Order, OrderAdmin)
