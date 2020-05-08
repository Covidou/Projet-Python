from django.shortcuts import render
from .models import Quizz


def home(request):
    context = {
        'quizzs': Quizz.objects.all()
    }
    return render(request, 'blog/home.html', context)

def apropos(request):
    return render(request, 'blog/apropos.html', {'title': 'À propos'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})
