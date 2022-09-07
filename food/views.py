from django.shortcuts import render
from .models import Foods
# Create your views here.

def about(request):
    return render(request,'food/about.html',{})


def blog_details(request):
    return render(request,'food/blog-details.html',{})


def blog(request):
    return render(request,'food/blog.html',{})


def contact(request):
    return render(request,'food/contact.html',{})


def gallery(request):
    return render(request,'food/gallery.html',{})


def index(request):
    food = Foods.objects.all()[:20]
    return render(request,'food/index.html',{'foods':food})


def menu(request):
    return render(request,'food/menu.html',{})


def reservation(request):
    return render(request,'food/reservation.html',{})


def stuff(request):
    return render(request,'food/stuff.html',{})


