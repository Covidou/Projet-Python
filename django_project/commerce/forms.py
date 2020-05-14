from django import forms
from .models import Product, Order

class BuyProductForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1, max_value=20)

    class Meta:
        model = Order
        fields = ['product', 'quantity']
