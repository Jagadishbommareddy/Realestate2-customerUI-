from django import forms
from .models import Customer
from .models import ContactInfo


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
