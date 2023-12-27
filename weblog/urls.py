from django.urls import path
from . import views

app_name = 'weblog'
urlpatterns = [
    path('<int:page>/',views.WeblogView.as_view(),name='blog')
]
