from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import PostCar, Comment


class AddCarForm(forms.ModelForm):
    """
    To create a form for the PostCar model to add more
    car post
    """

    class Meta:
        """
        Create fields to add post and select each field
        for styling. Content field includes summernotewidget
        for easy editing.
        """
        model = PostCar
        fields = (
            'car_model_title',
            'year_manufactured',
            'content',
            'car_image',
            'status',
        )
        widgets = {
            'car_model_title': forms.TextInput(
                attrs={
                    'class': 'form-control title-input'
                }
            ),
            'year_manufactured': forms.TextInput(
                attrs={
                    'class': 'form-control year-input'
                }
            ),
            'content': SummernoteWidget(
                attrs={'summernote': {
                    'max-width': '100%',
                    'data-device': 'iphone',
                }}
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control status-input'
                }
            ),
        }


class CommentForm(forms.ModelForm):
    """
    Create form for comments
    """
    class Meta:
        """
        Create fields to post comments
        """
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                }
            ),
        }
