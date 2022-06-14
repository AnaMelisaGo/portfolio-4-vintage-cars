from django.shortcuts import render
from django.views import generic, View
from django.core.paginator import Paginator
from .models import PostCar


class HomePageView(View):
    """ view home page """

    def get(self, request, *args, **kwargs):
        """ return homepage """
        context = {
            'home': 'active'
        }
        return render(request, 'home/index.html', context)


class CarPageView(View):
    """ Render the list of posted cars and display them to any user
        and separate the posts in pages, limiting the number of car posts in 6
        in each page """
    def get(self, request, *args, **kwargs):
        """ return cars page """
        post_car = PostCar.objects.filter(status=1).order_by('-date_created')
        paginator = Paginator(post_car, 6)

        page_number = request.GET.get('page')
        page_car = paginator.get_page(page_number)
        context = {
            'cars': 'active',
            'post_car': page_car
        }
        return render(request, 'cars.html', context)
