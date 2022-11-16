from email.policy import default
from tkinter import CASCADE
from django.db import models
from random import randint
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField




# Create your models here.


class Foods(models.Model):
    types = (
        ('lunch', 'lunch'),
        ('drinks', 'drinks'),
        ('dinner', 'dinner'),
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    type = models.CharField(max_length=6,choices=types,default="lunch")
    picture = models.ImageField(upload_to='food/', default='pic/default_food.png', null=True, blank=True)

    def __str__(self):
        return f"{self.name}  |  {self.description}"

#___________________________________________________________________________________________________________

class Reservation(models.Model):
    random_number = randint(100000,999999)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.name}  |  {self.email}  |  {self.date}"

#__________________________________________________________________________________________________________

class Blog(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    body = RichTextField(default='your blog text!')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='food/', null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="blog", blank=True, null=True)
    tags = models.ManyToManyField("Tag", related_name="blogs", blank=True)

    def __str__(self):
        return f"{self.title}  |  {self.body[:40]}  |  {self.date}"

# _________________________________________________________________________________________________________

class Category(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

# _________________________________________________________________________________________________________

class Tag(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    at = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return f"{self.title}"

# _________________________________________________________________________________________________________

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    time = models.TimeField(auto_now_add=True, auto_now=False)
    show_text = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}  |  {self.email}  |  {self.message}"

# _________________________________________________________________________________________________________


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_people = models.PositiveIntegerField(default=1)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}  |  {self.email}  |  {self.message[:50]}"


# _________________________________________________________________________________________________________

class Reply(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    time = models.TimeField(auto_now_add=True, auto_now=False)
    show_text = models.BooleanField(default=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}  |  {self.email}  |  {self.message[:50]}"


# _________________________________________________________________________________________________________


class Gallery(models.Model):
    image = models.ImageField(upload_to='food/',)

    def __str__(self):
        return f"{self.image}"


# _________________________________________________________________________________________________________


class Stuff(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30, default="+01", blank=True, null=True)
    image = models.ImageField(upload_to='food/',default='pic/worker.jpg', blank=True, null=True,)

    def __str__(self):
        return f"{self.name}  |  {self.job}"