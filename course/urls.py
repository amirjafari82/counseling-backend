from django.urls import path, re_path
from . import views

app_name = 'course'

urlpatterns = [
    path('<int:page>/',views.CourseList.as_view(),name='course-list'),
    path('<int:page>/<str:category>/',views.CategoryFilterView.as_view(),name='course-filter'),
    re_path(r'(?P<slug>[^/]+)/?$',views.CourseDetailView.as_view(),name='course-detail'),
]
