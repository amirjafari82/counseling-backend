from django.db import models
from django_jalali.db import models as jmodels


CATEGORY_CHOICES = (
    ("Men","مشاوره آقایان"),
    ("Couples","مشاوره زوجین"),
    ("Women","مشاوره خانم ها"),
)


class Teacher(models.Model):
    image = models.ImageField(upload_to='static/images/teachers',default=None)
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=150, verbose_name="University education")
    intro = models.TextField(verbose_name="Teacher Introduction")
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(choices=CATEGORY_CHOICES,max_length=50)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        if self.name == 'Men':
            return "مشاوره آقایان"
        if self.name == 'Couples':
            return "مشاوره زوجین"
        if self.name == 'Women':
            return "مشاوره خانم ها"
    

class Course(models.Model):
    image = models.ImageField(upload_to='static/images/course',default=None)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='course_category')
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='course_teacher')
    slug = models.SlugField(auto_created=True,unique=True,allow_unicode=True,default=None)
    desc = models.TextField()
    fewdesc = models.TextField(default=None)
    price = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    students = models.IntegerField(default=0)
    sessions = models.IntegerField(default=0)
    created = jmodels.jDateTimeField(auto_now_add=True,blank=True,null=True)