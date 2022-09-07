from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path("about/",views.about,name="about"),
    path("blog_details/",views.blog_details,name="blog_details"),
    path("blog/",views.blog,name="blog"),
    path("contact/",views.contact,name="contact"),
    path("gallery/",views.gallery,name="gallery"),
    path("menu/",views.menu,name="menu"),
    path("reservation/",views.reservation,name="reservation"),
    path("stuff/",views.stuff,name="stuff"),
]
