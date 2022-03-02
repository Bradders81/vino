from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'address_line1',
                  'address_line2', 'city_town', 'postcode',)


    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and removed labels generated
        by django forms
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'address_line1': 'Street Address 1',
            'address_line2': 'Street Address 2',
            'postcode': 'Postal Code',
            'town_city': 'Town or City',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
