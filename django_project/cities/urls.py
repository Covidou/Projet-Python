from django.urls import path
from . import views

urlpatterns = [
    path('chartJSON', views.line_chart_json, name='line_chart_json'),
    path('<str:commune>', views.dataviz, name='cities-dataviz'),
]
