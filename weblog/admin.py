from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','views','created']
    search_fields = ['title','body']
    list_filter = ['created']