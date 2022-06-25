import django_filters
from django_filters import CharFilter, BooleanFilter
from django_filters.widgets import BooleanWidget
from cars.models import PostCar


class CanRentWidget(BooleanWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = (
            ("Unknown", ("All")), ("true", ("Yes")), ("false", ("No"))
        )


class PostCarFilter(django_filters.FilterSet):
    """ filter """
    car_model_title = CharFilter(
        field_name='car_model_title', lookup_expr='icontains'
    )
    can_rent = BooleanFilter(widget=CanRentWidget)

    class Meta:
        """ class meta filter """
        model = PostCar
        fields = {'car_model_title', 'status', 'can_rent'}
