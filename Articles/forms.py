from django import forms
from django.forms import ModelForm
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#LOGIN FORM

class LoginForm(forms.Form):

    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)

#REGISTRATION FORM 
   
class UserRegistration(UserCreationForm):
    #username= forms.CharField(label='User Name', max_length=16, min_length=4, required=True, error_messages={"username_exists":"Username alrready exists."})
    #First_name= forms.CharField(label='First Name', max_length=30, required=False)
    #Last_name= forms.CharField(label='Last Name', max_length=30, required=False)
    #email= forms.CharField(label='Email', max_length=100, required=True, error_messages={"invalid":"Please, enter correct E-mail."})
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class ArticleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description']


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model= Article
        fields= ['title','description']