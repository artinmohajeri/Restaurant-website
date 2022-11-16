from django import forms
from .models import Reservation,Comment,Contact,Reply

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields= "__all__"

# __________________________________________________________________

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ["name", "email", "message",]

# __________________________________________________________________


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields= ["name", "email", "message",]

# __________________________________________________________________

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= "__all__"