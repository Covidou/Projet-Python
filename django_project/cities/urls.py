from django.urls import path
from . import views

urlpatterns = [
    path('chartJSON/<str:commune>', views.retrieve_data, name='retrieve_data'),
    path('<str:commune>', views.dataviz, name='cities-dataviz'),
]
