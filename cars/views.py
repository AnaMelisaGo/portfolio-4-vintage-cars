from django.shortcuts import render, get_object_or_404
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
            'post_car': page_car,
        }
        return render(request, 'cars/cars.html', context)


class CarDetail(View):
    """ 
    To view all post in cars page
    --- more------------------------------------------------------------
    """
    def get(self, request, post_id, *args, **kwargs):
        """ docstring """
        queryset = PostCar.objects.filter(status=1)
        post_car = get_object_or_404(queryset, pk=post_id)
        comments = post_car.comments.filter(
            post_id=post_id).order_by('date_created')
        liked = False
        if post_car.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "cars/car_detail.html",
            {
                'cars': 'active',
                'post_car': post_car,
                'comments': comments,
                'liked': liked,
            }
        )


class AddCarPost(View):
    """ To add a post about a car """

    def get(self, request, *args, **kwargs):
        """
        To post a car and view
        """
        context = {
            'cars': 'active'
        }
        return render(request, 'cars/add_car.html', context)
