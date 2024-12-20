from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

from application.models import Order

SELECT_PACKAGE = [
    ('mombasa','Mombasa Value'),
    ('diani','Diani Classic'),
    ('malindi','Malindi Deluxe'),
    ('bugdets','Bugdets Safari'),
    ('mid-range','Mid-Range Safari'),
    ('luxury','Luxury Safari'),
    ('meru','Meru Value'),
    ('nyeri','Nyeri Comfort'),
    ('nanyuki','Nanyuki Exclusive'),
]
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {

            'full_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your full name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Add your contact number'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your email'}),
            'checkin_date': forms.TextInput(attrs={'class': 'form-control','placeholder': 'DD/MM/YYYY'}),
            'checkout_date': forms.TextInput(attrs={'class': 'form-control','placeholder': 'DD/MM/YYYY'}),
            'number_of_adults': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Add adults travelling'}),
            'number_of_children': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Add children travelling'}),
            'select_package': forms.Select(choices=SELECT_PACKAGE, attrs={'class': 'form-control', 'placeholder': 'Select package'}),
            'trip_preferences': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your trip preferences'}),



        }



