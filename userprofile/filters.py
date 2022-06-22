import django_filters
from django_filters import CharFilter
from cars.models import PostCar


class PostCarFilter(django_filters.FilterSet):
    """ filter """
    car_model_title = CharFilter(
        field_name='car_model_title', lookup_expr='icontains'
    )
    year_manufactured = CharFilter(
        field_name='year_manufactured', lookup_expr='iexact'
    )

    class Meta:
        """ class meta filter """
        model = PostCar
        fields = {'car_model_title', 'year_manufactured', 'status'}
