from django import forms
from .models import UserReview


class UserReviewForm(forms.ModelForm):
    """
    Form for users to add a review of a product.
    """
    class Meta:
        model = UserReview
        fields = '__all__'
        exclude = ('user_profile',)

    def __init__(self, *args, **kwargs):
        super(UserReviewForm, self).__init__(*args, **kwargs)

        placeholders = {
            'review_name': 'review_name',
            'wine': 'wine',
            'score': 'score',
            'review': 'review',
            'buy_again': 'buy_again',
        }

        self.fields['review_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
