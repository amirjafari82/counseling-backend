from django.contrib import admin
from .models import Course, Teacher, Category, Comment, CommentAnswer

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','teacher','created']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title','teacher','desc']
    list_filter = ['created']
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','course','body','score']
    search_fields = ['user','course','body']
    
@admin.register(CommentAnswer)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['answer']
    search_fields = ['answer']