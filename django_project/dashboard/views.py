from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html')

def apropos(request):
    return render(request, 'dashboard/apropos.html', {'title': 'À propos'})

def contact(request):
    return render(request, 'dashboard/contact.html', {'title': 'Contact'})

