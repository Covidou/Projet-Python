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
            user.profile.code_postal = int(form.cleaned_data.get('code_postal'))
            print(form.cleaned_data.get('code_postal'))
            user.profile.ville = form.cleaned_data.get('ville')
            print(form.cleaned_data.get('ville'))
            user.profile.addresse = form.cleaned_data.get('addresse')
            user.profile.num_tel = form.cleaned_data.get('num_tel')
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte {username} a ete cree, vous pouvez maintenant vous authentifier')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
