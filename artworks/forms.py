from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Artwork, Review


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = [
            "title",
            "featured_image",
            "description",
            "topic",
            "demo_link",
            "source_link",
            # "tags",
        ]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ArtworkForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'Sum_it_up', 'What_works', 'What_needs_work', 'What_might_work']

        labels = {
            'rating': 'How many stars?',
            'Sum_it_up': 'Add a brief headline',
            'What_works': 'Positive feedback:',
            'What_needs_work': 'Specific, critical feedback:',
            'What_might_work': 'A potential direction for the work:'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
