from django.contrib import admin
from django.urls import path, include
from talktale import views

urlpatterns = [
    path('', views.index, name='talktale'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blogs', views.blogs, name='blogs'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
    path('thanks', views.thanks, name='thanks'),
]