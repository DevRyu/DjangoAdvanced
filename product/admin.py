from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    # 폴더,모델의 클래스명 순으로
    list_display = ('name', 'price')


admin.site.register(Product, ProductAdmin)
