from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.utils.encoding import uri_to_iri
from django.core.paginator import Paginator
from .models import Article


class WeblogView(View):
    
    def get(self,request,page):
        top_views_articles = Article.objects.all().order_by('-views')
        latest_articles = Article.objects.all().order_by('-created')
        paginator = Paginator(latest_articles,per_page=6)
        page_obj = paginator.get_page(page)
        return render(request,'weblog/index.html',{'top_articles':top_views_articles,'latest_articles':latest_articles,'page_obj':page_obj})
    

class ArticleDetailView(View):
    
    def get(self,request,slug):
        article = get_object_or_404(Article,slug=uri_to_iri(slug))
        article.views += 1
        article.save()
        related_articles = Article.objects.filter(category=article.category).exclude(id=article.id)
        return render(request, 'weblog/article.html',{'article':article,'related':related_articles})