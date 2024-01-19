from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','phone','password')
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder':'نام'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'نام خانوادگی'}),
            'phone' : forms.TextInput(attrs={'placeholder':'شماره تماس'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'رمز عبور','id':'password'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'شماره موبایل','id':'phoneNumber'}),error_messages={'required':'فیلد شماره موبایل الزامی است'})
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور','id':'password'}),error_messages={'required':'فیلد رمز عبور الزامی است'})