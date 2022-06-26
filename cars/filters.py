import django_filters
from django_filters import CharFilter, BooleanFilter
from django_filters.widgets import BooleanWidget
from django.forms.widgets import TextInput
from .models import PostCar


class CanRentWidget(BooleanWidget):
    """
    Change the choices in the dropdown choices when filtering cars for rent
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = (
            ("Unknown", ("All")), ("true", ("Yes")), ("false", ("No"))
        )


class PostCarFilter(django_filters.FilterSet):
    """ filter """
    car_model_title = CharFilter(
        field_name='car_model_title',
        lookup_expr='icontains',
        label='Car Model',
        widget=TextInput(attrs={'placeholder': 'Car Model'}),
    )
    year_manufactured = CharFilter(
        field_name='year_manufactured',
        lookup_expr='lte',
        label='Year manufactured',
        widget=TextInput(attrs={'placeholder': 'min'}),
    )
    year_manufactured_min = CharFilter(
        field_name='year_manufactured',
        lookup_expr='gte',
        label='Year manufactured',
        widget=TextInput(attrs={'placeholder': 'max'}),
    )
    can_rent = BooleanFilter(widget=CanRentWidget)

    class Meta:
        """ class meta filter """
        model = PostCar
        fields = {'car_model_title', 'year_manufactured', 'can_rent'}
