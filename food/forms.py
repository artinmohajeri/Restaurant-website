from django import forms
from .models import Reservation,Comment,Contact

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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= "__all__"