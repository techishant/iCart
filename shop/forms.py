from django import forms
from django.forms import widgets

class addProd(forms.Form):
    Product_Name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class':"form-control","placeholder":"Product Name"}))
    Image = forms.FileField(required=True, widget=forms.FileInput(attrs={'class':'form-control'}))
    Description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'cols':"", "rows":"5", "placeholder":"Product Description"}))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'min':1, "placeholder":"Product Price"}))