from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Doc string
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and removed labels generated
        by django forms
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number',
            'address_line1': 'Street Address 1',
            'address_line2': 'Street Address 2',
            'postcode': 'Postal Code',
            'city_town': 'Town or City',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
