from django import forms
from django.forms import ModelForm
from .models import Service, Category, Doctor


# Create a Service form
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('category', 'name', 'image', 'description', 'price')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'image','category')

        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }