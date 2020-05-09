from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('apropos/', views.apropos, name='dashboard-apropos'),
    path('contact/', views.contact, name='dashboard-contact'),
]
