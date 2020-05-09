from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BuyProductForm
from django.contrib import messages

@login_required
def buy(request):
    if request.method == 'POST':
        form = BuyProductForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, f'Vous avez acheté {order.quantity} {order.product}')
            return redirect('buy')
    else:
        form = BuyProductForm()
    return render(request, 'commerce/buy.html', context={'buy_form': form})