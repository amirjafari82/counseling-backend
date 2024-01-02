from django.contrib import admin
from .models import Article, Author, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','views','created']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title','body']
    list_filter = ['created']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']