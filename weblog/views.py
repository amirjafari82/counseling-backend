from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .models import Article


class WeblogView(View):
    
    def get(self,request,page):
        top_views_articles = Article.objects.all().order_by('-views')
        latest_articles = Article.objects.all()
        paginator = Paginator(latest_articles,per_page=6)
        page_obj = paginator.get_page(page)
        return render(request,'weblog/index.html',{'top_articles':top_views_articles,'latest_articles':latest_articles,'page_obj':page_obj})