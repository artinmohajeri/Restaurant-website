from django.shortcuts import render,get_object_or_404,redirect
from .models import Category, Contact, Foods, Reply,Reservation,Blog,Tag,Comment,Gallery,Stuff
from .forms import CommentForm, ContactForm, ReplyForm, ReservationForm
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

    paginator = Paginator(blogs, 6)
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
            contact_form.save()

    else:
        contact_form = ContactForm()

    context = {

    }

    return render(request,'food/contact.html',context)

#___________________________________________________________________________________________________________


def gallery(request):
    pics = Gallery.objects.all()
    return render(request,'food/gallery.html',{'pics':pics})

#___________________________________________________________________________________________________________


def index(request):
    food = Foods.objects.all()[:9]
    pics = Gallery.objects.all()[:6]
    return render(request,'food/index.html',{'foods':food,'pics':pics})

#___________________________________________________________________________________________________________


def menu(request):
    foods = Foods.objects.all()

    context = {
        'foods':foods
    }
    return render(request,'food/menu.html',context)

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
    worker = Stuff.objects.all()

    context = {
        'stuff':worker,
    }
    return render(request,'food/stuff.html',context)

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

def reply(request, id):
    comment = get_object_or_404(Comment, id=id)
    replies = Reply.objects.all().filter(comment=comment)

    reply_form = ReplyForm()
    if request.method == "POST":
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply_form.save()
            return redirect('blog')
        
    else:
        reply_form = ReplyForm()

    context={
        "replies":replies
    }

    return render(request,'food/reply.html',context)






