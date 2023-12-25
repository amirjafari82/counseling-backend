from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import ContactForm


class ContactUsView(View):
    form_class = ContactForm
    
    def get(self,request):
        return render(request,'contactus/index.html',{'form':self.form_class})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'پیام شما با موفقیت ارسال شد','success')
        return redirect('home:home')