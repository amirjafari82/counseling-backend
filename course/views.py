from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.utils.encoding import uri_to_iri
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Course, Category, Comment, CommentAnswer
from .forms import CommentForm


class CourseList(View):
    
    def get(self,request,page):
        category = self.request.GET.get('category')
        print(category)
        if category:
            courses = Course.objects.filter(category__name=category)
        courses = Course.objects.all()
        paginator = Paginator(courses,per_page=6)
        page_obj = paginator.get_page(page)
        categories = Category.objects.all()
        return render(request,'course/course-list.html',{'page_obj':page_obj,'categories':categories})
    

class CategoryFilterView(View):
    
    def get(self,request,page,category):
        categories = Category.objects.all()
        category_ins = Category.objects.get(name=category)
        courses = Course.objects.filter(category=category_ins.pk)
        paginator = Paginator(courses,per_page=6)
        page_obj = paginator.get_page(page)
        category_ins.active = True
        category_ins.save()
        return render(request,'course/course-list.html',{'page_obj':page_obj,'categories':categories,'category_ins':category_ins})
    

class CourseDetailView(View):
    
    def get(self,request,slug):
        course = get_object_or_404(Course,slug=uri_to_iri(slug))
        comments = Comment.objects.filter(course=course,approved=True)
        comments_answer = CommentAnswer.objects.all()
        return render(request,'course/course-detail.html',{'course':course,'comments':comments})
    
    def post(self,request,slug):
        course = Course.objects.get(slug=uri_to_iri(slug))
        score = self.request.POST.get('val')
        body = self.request.POST.get('body')
        user = request.user
        if body == None:
            return redirect('course:course-detail',slug)
        new_comment = Comment.objects.create(user=user,score=score,body=body,course=course)
        new_comment.save()
        messages.success(request,'کامنت شما با موفقیت ثبت شد و در انتظار تایید است. باتشکر','success')
        return JsonResponse({'status':'ok'})