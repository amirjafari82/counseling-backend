from django.db import models
from django_jalali.db import models as jmodels


class Article(models.Model):
    image = models.ImageField(upload_to='static/images/weblog',default=None)
    title = models.CharField(max_length=120)
    pers = models.TextField()
    body = models.TextField()
    views = models.IntegerField(default=0)
    created = jmodels.jDateTimeField(auto_now_add=True,blank=True,null=True)