from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('apropos/', views.apropos, name='blog-apropos'),
    path('contact/', views.contact, name='blog-contact'),
]
