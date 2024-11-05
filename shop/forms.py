from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the name of product'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the details'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Enter the image'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose the category'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the stock'}),
        }

