from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
# 콤마를 안쓰면 튜플로 인식 못하므로 주의하자!


admin.site.register(User, UserAdmin)
