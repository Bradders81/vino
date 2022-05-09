from django import forms
from .models import UserReview

class UserReviewForm(forms.ModelForm):
    """
    Form for users to add and edit a review of a product.
    """
    class Meta:
        model = UserReview
        fields = '__all__'
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        super(UserReviewForm, self).__init__(*args, **kwargs)

        placeholders = {
            'review_name': 'Review Title',
            'wine': 'wine',
            'review': 'Write you review here.....',
            'buy_again': 'Buy Again?',
            'user': 'username',
        }

        self.fields['review_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
