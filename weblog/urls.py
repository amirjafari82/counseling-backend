from django.urls import path, re_path
from . import views

app_name = 'weblog'
urlpatterns = [
    path('<int:page>/',views.WeblogView.as_view(),name='blog'),
    re_path(r'(?P<slug>[^/]+)/?$',views.ArticleDetailView.as_view(),name='article'),
]
