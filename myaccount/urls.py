from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'), 
    path('accoustic/', views.accoustic, name='accoustic'), 
    path('classic/', views.classic, name='classic'), 
    path('elektrik/', views.elektrik, name='elektrik'), 
    path('upload/', views.upload, name='upload'),
    path('cate/', views.cate, name="cate"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

]