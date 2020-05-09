from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.postal_code = form.cleaned_data.get('postal_code')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte {username} a ete cree, vous pouvez maintenant vous authentifier')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
