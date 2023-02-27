from django import forms
from .models import Review
from django.forms import ModelForm

# class Review(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=200)
#     last_name = forms.CharField(label='Last Name', max_length=200)
#     email = forms.EmailField(label="Email")
#     review = forms.CharField(label="Please write your review")

class Review(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name','last_name','stars']