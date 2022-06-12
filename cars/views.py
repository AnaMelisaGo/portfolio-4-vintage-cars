from django.shortcuts import render
from django.views import generic, View
from .models import PostCar


class HomePageView(View):
    """ view home page """

    def get(self, request, *args, **kwargs):
        """ return homepage """
        context = {
            'home': 'active'
        }
        return render(request, 'home/index.html', context)


class PostCarList(generic.ListView):
    """ Render the list of posted cars and display them to any user
    and separate the posts in pages, limiting the number of car posts in 6
    in each page """
    model = PostCar
    queryset = PostCar.objects.filter(status=1).order_by('-date_created')
    template_name = 'cars.html'
    paginated_by = 6
