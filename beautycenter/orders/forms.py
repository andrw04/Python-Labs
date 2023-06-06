from django import forms
from .models import Order
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date, datetime

def validate_age(value):
    today = date.today()
    age = today.year - value.year - int((today.month, today.day) < (value.month, value.day))
    print(today.year)
    print(value.year)
    print(age)
    if int(age) < 18:
        raise ValidationError("Your age should be greater than 18")


class OrderCreateForm(forms.ModelForm):
    birth_date = forms.DateField(validators=[validate_age])
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'birth_date', 'mobile']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
