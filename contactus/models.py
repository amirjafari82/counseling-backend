from django.db import models
from django_jalali.db import models as jmodels

SITUATION_CHOICES = (
    ("Pending","Pending"),
    ("In Progress","In Progress"),
    ("Solved","Solved")
)

class Contact(models.Model):
    first_name = models.CharField(verbose_name="First Name",max_length=20)
    last_name = models.CharField(verbose_name="Last Name",max_length=20)
    phone = models.CharField(verbose_name="Last Name",max_length=11)
    email = models.EmailField(verbose_name="Email",max_length=100)
    desc = models.TextField(verbose_name="Description",blank=True,null=True)
    situation = models.CharField(max_length=30,choices=SITUATION_CHOICES,default='Pending')
    created = jmodels.jDateTimeField(auto_now_add=True,blank=True,null=True)