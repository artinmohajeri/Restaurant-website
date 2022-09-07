from django.contrib import admin
from .models import Foods
# Register your models here.


@admin.register(Foods)
class FoodsAdmin(admin.ModelAdmin):
    pass

