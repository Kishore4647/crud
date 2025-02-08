# forms.py
from django import forms

class OrderForm(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput,max_length=150)
    address = forms.CharField(widget=forms.TextInput, max_length=100)
    quantity=forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'step': 1}),
        label='Quantity',
        initial=1
    )


    
