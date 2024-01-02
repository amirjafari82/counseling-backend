from django.db import models
from django_jalali.db import models as jmodels
    

class Author(models.Model):
    image = models.ImageField(upload_to='static/images/authors',default=None)
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=150,verbose_name="University education")
    intro = models.TextField()
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Article(models.Model):
    image = models.ImageField(upload_to='static/images/weblog',default=None)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='article_category')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='article_author')
    pers = models.TextField()
    body = models.TextField()
    slug = models.SlugField(auto_created=True,unique=True,allow_unicode=True,default=None)
    views = models.IntegerField(default=0)
    created = jmodels.jDateTimeField(auto_now_add=True,blank=True,null=True)