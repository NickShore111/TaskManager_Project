from django.forms import ModelForm
from reviews.models import Reviews

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        exclude = ['created_at']