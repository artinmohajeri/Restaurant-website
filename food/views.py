from django.shortcuts import render,get_object_or_404
from .models import Category, Foods,Reservation,Blog,Tag
from .forms import ReservationForm
from random import randint
# Create your views here.

def about(request):
    return render(request,'food/about.html',{})


def blog_details(request ,id):
    b = get_object_or_404(Blog, id=id)
    tags = Tag.objects.all()
    recent = Blog.objects.all().order_by("-date")
    category = Category.objects.all()
    context = {
        'blog' : b,
        'tags':tags,
        'recent':recent,
        'categorys':category,

    }
    return render(request,'food/blog-details.html',context)


def blog(request):
    blogs = Blog.objects.all()[:20]
    return render(request,'food/blog.html',{'blogs':blogs})


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
    reservation_form = ReservationForm()
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid():
            reservation_form.save()
    else:
        reservation_form = ReservationForm()

    return render(request,'food/reservation.html',{'form':reservation_form,})


def stuff(request):
    return render(request,'food/stuff.html',{})


