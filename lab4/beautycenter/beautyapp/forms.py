from django.forms import ModelForm
from .models import Category, Service, Order, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


# class PlannedVisitForm(ModelForm):
#     class Meta:
#         model = PlannedVisit
#         fields = '__all__'


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


# class PriceListForm(ModelForm):
#     class Meta:
#         model = PriceList
#         fields = '__all__'


# class SaleForm(ModelForm):
#     class Meta:
#         model = Sale
#         fields = '__all__'


# class OfficeForm(ModelForm):
#     class Meta:
#         model = Office
#         fields = '__all__'


# class DoctorForm(ModelForm):
#     class Meta:
#         model = Doctor
#         fields = '__all__'


# class ScheduleForm(ModelForm):
#     class Meta:
#         model = Schedule
#         fields = '__all__'


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })

        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your address'
        })
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your birth date'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })

    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    address = forms.CharField(max_length=150)
    birth_date = forms.DateField(widget=forms.DateInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','address','birth_date', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'birth_date')


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client']
    
# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'