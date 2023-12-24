from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone", "email", "desc")
        labels = {
            'first_name': '',
            'last_name': '',
            'phone': '',
            'email': '',
            'desc': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'نام'}),
            'last_name': forms.TextInput(attrs={'placeholder':'نام خانوادگی'}),
            'phone': forms.TextInput(attrs={'placeholder':'شماره تماس'}),
            'email': forms.TextInput(attrs={'placeholder':'ایمیل'}),
            'desc': forms.Textarea(attrs={'placeholder':'توضیحات (اختیاری)','cols':'0','rows':'0'}),
        }
