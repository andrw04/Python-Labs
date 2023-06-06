from django import forms
from django.forms import ModelForm
from .models import Service, Category, Doctor
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date, datetime


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


def validate_age(value):
    today = date.today()
    age = today.year - value.year - int((today.month, today.day) < (value.month, value.day))
    print(today.year)
    print(value.year)
    print(age)
    if int(age) < 18:
        raise ValidationError("Your age should be greater than 18")


class DoctorForm(ModelForm):
    birth_date = forms.DateField(validators=[validate_age])
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'image', 'birth_date', 'category')

        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
        }