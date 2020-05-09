from django import forms
from .models import Product, Order

class BuyProductForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField()

    class Meta:
        model = Order
        fields = ['product', 'quantity']
