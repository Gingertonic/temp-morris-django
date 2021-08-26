from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'cat']

class UpdateQuantityForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quantity']
        widgets = { 'quantity': forms.HiddenInput }