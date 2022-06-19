from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import PostCar


class AddCarForm(forms.ModelForm):
    """
    To create a form for the PostCar model to add more
    car post
    """

    class Meta:
        """
        Create fields and select each for styling
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
                attrs={'class': 'form-control title-input transparent-bg t-white'}
            ),
            'year_manufactured': forms.TextInput(
                attrs={'class': 'form-control year-input transparent-bg t-white'}
            ),
            'content': SummernoteWidget(),
            'status': forms.Select(
                attrs={'class': 'form-control status-input transparent-bg t-white'}
            ),
        }
