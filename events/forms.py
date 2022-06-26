from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Event, EventComment


class EventForm(forms.ModelForm):
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
        model = Event
        fields = (
            'event_title',
            'location',
            'event_date',
            'event_excerpt',
            'content',
            'event_image'
        )
        widgets = {
            'event_title': forms.TextInput(
                attrs={
                    'class': 'form-control title-input'
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control title-input'
                }
            ),
            'event_date': forms.DateInput(
                attrs={
                    'class': 'datepicker year-input'
                }
            ),
            'event_excerpt': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                }
            ),
            'content': SummernoteWidget(
                attrs={'summernote': {
                    'width': '100%',
                }}
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
        model = EventComment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                }
            ),
        }
