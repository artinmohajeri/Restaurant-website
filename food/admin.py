from django.contrib import admin
from .models import Foods,Reservation,Blog,Category,Tag,Comment,Contact
# Register your models here.


@admin.register(Foods)
class FoodsAdmin(admin.ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


