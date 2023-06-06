from django import forms


class CartAddServiceForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)