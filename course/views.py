from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.encoding import uri_to_iri
from django.core.paginator import Paginator
from .models import Course, Category


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
        return render(request,'course/course-list.html',{'page_obj':page_obj,'categories':categories,'category_ins':category_ins})
    

class CourseDetailView(View):
    
    def get(self,request,slug):
        course = get_object_or_404(Course,slug=uri_to_iri(slug))
        return render(request,'course/course-detail.html',{'course':course})