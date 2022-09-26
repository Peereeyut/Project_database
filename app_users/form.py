from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from app_users.models import Profile



class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )


class Userprofile(forms.ModelForm):
    class Meta:
        model = User
        fields =("first_name", 'last_name', 'email' )

class ExtendedProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("address", "phone")

        widgets ={
            "address":forms.Textarea(attrs={"rows":3})
        }