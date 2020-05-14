from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html')

def contact(request):
    return render(request, 'dashboard/contact.html', {'title': 'Contact'})

