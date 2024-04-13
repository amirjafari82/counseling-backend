from django.urls import path, re_path
from . import views

app_name = 'course'

urlpatterns = [
    path('<int:page>/',views.CourseList.as_view(),name='course-list'),
    re_path(r'(?P<slug>[^/]+)/?$',views.CourseDetailView.as_view(),name='course-detail'),
]
