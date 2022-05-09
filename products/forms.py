from django import forms
from .models import Wine


class ProductForm(forms.ModelForm):
    """
    Form for superuser/site owner to
    update products.
    |"""

    class Meta:
        model = Wine
        fields = '__all__'
