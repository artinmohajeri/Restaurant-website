from django.contrib import admin
from .models import Foods,Reservation,Blog,Category, Stuff,Tag,Comment,Contact,Reply,Gallery
# Register your models here.


@admin.register(Foods)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ('name','description','price')
    list_filter = ('name','price',)
    search_fields = ('name','description','price',)
    ordering = ('price',)

    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone_number','number_of_people')
    list_filter = ('name','email','date')
    search_fields = ('name','email','phone_number',)
    ordering = ('number_of_people',)

    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','date','author','category')
    list_filter = ('date','author','title',)
    search_fields = ('title','date','author',)
    ordering = ('date',)

    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','time')
    list_filter = ('time','name','email',)
    search_fields = ('name','email','time',)
    ordering = ('time',)


    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','number_of_people')
    list_filter = ('name','email','number_of_people',)
    search_fields = ('name','email','number_of_people',)
    ordering = ('number_of_people',)
    pass

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    search_fields = ('image',)
    pass

@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('name','job',)
    search_fields = ('name','job',)
    list_filter = ('name','job',)
    ordering = ('name',)
    pass



