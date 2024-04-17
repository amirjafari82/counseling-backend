from django.db import models
from django_jalali.db import models as jmodels
from django.core.validators import MaxValueValidator,MinValueValidator
from accounts.models import User


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
    recommended = models.TextField(default=None)
    created = jmodels.jDateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
class CommentAnswer(models.Model):
    answer = models.TextField(max_length=200)
    
    def __str__(self):
        return self.answer
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='course_comment')
    body = models.TextField(max_length=200)
    score = models.IntegerField(default=0,validators=
        [
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    approved = models.BooleanField(default=False)
    answer = models.ForeignKey(CommentAnswer,on_delete=models.CASCADE,related_name='comment_answer',blank=True,null=True)
    answered = models.BooleanField(default=False)
    created = jmodels.jDateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.body[:20]}'