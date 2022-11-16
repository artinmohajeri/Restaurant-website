from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path("about/",views.about,name="about"),
    path("blog/<int:id>",views.blog_details,name="blog_details"),
    path("blogs/",views.blog,name="blog"),
    path("contact/",views.contact,name="contact"),
    path("gallery/",views.gallery,name="gallery"),
    path("menu/",views.menu,name="menu"),
    path("search/",views.search,name="search"),
    path("reservation/",views.reservation,name="reservation"),
    path("stuff/",views.stuff,name="stuff"),
    path("reply/<int:id>",views.reply,name="reply"),
    path("blogs/tag/<slug:tag>",views.blog_tag,name="blog_tag"),
    path("blogs/category/<slug:category>",views.blog_category,name="blog_category"),
]
