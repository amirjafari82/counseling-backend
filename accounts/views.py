from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.views import View
from django.contrib.auth.views import LogoutView 
from .forms import SignupForm, LoginForm


class SignupView(View):
    form_class = SignupForm
    
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home:home')
        return render(request,'accounts/signup.html',{'form':self.form_class})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(phone=phone,first_name=first_name,last_name=last_name,password=password)
            messages.success(request,'حساب شما با موفقیت ساخته شد','success')
            return redirect('accounts:login')
        else:
            messages.error(request,'این شماره قبلا ثبت شده است','danger')
            return redirect('accounts:signup')
        
class LoginView(View):
    form_class = LoginForm
    
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home:home')
        return render(request,'accounts/login.html',{'form':self.form_class})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                    messages.success(request,'وارد شدید','success')
                    login(request,user)
                    return redirect('home:home')
            else:
                messages.error(request,'شماره تماس یا رمز عبور اشتباه است','danger')
                return redirect('accounts:login')
        return redirect('home:home')
    
class UserLogout(LogoutView):
    next_page = reverse_lazy('home:home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request,'خارج شدید','success')
        return super().dispatch(request, *args, **kwargs)