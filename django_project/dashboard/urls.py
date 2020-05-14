from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('contact/', views.contact, name='dashboard-contact'),
]
