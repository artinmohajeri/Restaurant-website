from django.shortcuts import render,get_object_or_404
from .models import Category, Contact, Foods,Reservation,Blog,Tag,Comment
from .forms import CommentForm, ContactForm, ReservationForm
from random import randint
from django.core.paginator import Paginator
# Create your views here.


#___________________________________________________________________________________________________________

def about(request):
    return render(request,'food/about.html',{})

#___________________________________________________________________________________________________________


def blog_details(request ,id):
    blog = get_object_or_404(Blog, id=id)
    tags = Tag.objects.all()
    recent = Blog.objects.all().order_by("-date")
    category = Category.objects.all()
    comments = Comment.objects.all().filter(blog=blog)

    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            name = comment.cleaned_data["name"]
            email = comment.cleaned_data["email"]
            message = comment.cleaned_data["message"]

            new_comment = Comment(name=name, email=email, message=message, blog=blog)
            new_comment.save()

        else:
            comment = CommentForm()
        
    context = {
        'blog' : blog,
        'tags':tags,
        'recent':recent,
        'categorys':category,
        'comments':comments,
    }
    return render(request,'food/blog-details.html',context)

#___________________________________________________________________________________________________________


def blog(request):
    blogs = Blog.objects.all()
    default = range(1,5)

    paginator = Paginator(blogs, 1)
    page = request.GET.get('page')
    blog_list = paginator.get_page(page)
    
    context = {
        'blogs':blogs,
        "blog_list":blog_list,
        "default":default,
        }

    return render(request,'food/blog.html',context)

#___________________________________________________________________________________________________________


def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            numbers = contact_form.cleaned_data["number_of_people"]
            message = contact_form.cleaned_data["message"]

            new_contact = Contact(name=name, email=email, message=message, number_of_people=numbers)
            new_contact.save()
    else:
        contact_form = ContactForm()

    context = {

    }

    return render(request,'food/contact.html',{})

#___________________________________________________________________________________________________________


def gallery(request):
    return render(request,'food/gallery.html',{})

#___________________________________________________________________________________________________________


def index(request):
    food = Foods.objects.all()[:20]
    return render(request,'food/index.html',{'foods':food})

#___________________________________________________________________________________________________________


def menu(request):
    return render(request,'food/menu.html',{})

#___________________________________________________________________________________________________________


def reservation(request):
    reservation_form = ReservationForm()
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid():
            reservation_form.save()
    else:
        reservation_form = ReservationForm()

    return render(request,'food/reservation.html',{'form':reservation_form,})

#___________________________________________________________________________________________________________


def stuff(request):
    return render(request,'food/stuff.html',{})

#___________________________________________________________________________________________________________


def blog_tag(request, tag):

    blogs = Blog.objects.filter(tag__slug = tag)
    context = {
        'blogs':blogs,

        }
    return render(request,'food/blog-details.html',context)

#___________________________________________________________________________________________________________


def blog_category(request, category):

    blogs = Blog.objects.filter(category__slug = category)
    context = {
        'blogs':blogs,

        }
    return render(request,'food/blog-details.html',context)


#___________________________________________________________________________________________________________


def search(request):

    if request.method == "GET":
        value = request.GET.get('search')
        blog_list = Blog.objects.filter(body__icontains = value)

    context = {
        "blog_list":blog_list
    }

    return render(request,'food/blog.html',context)

#___________________________________________________________________________________________________________







