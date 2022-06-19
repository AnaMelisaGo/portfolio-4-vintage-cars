from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from .models import PostCar
from .forms import AddCarForm, CommentForm

from cloudinary.forms import cl_init_js_callbacks


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
    To view the post's page. It displays the photo,
    content, author and date created
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
                'comment_form': CommentForm(),
                'comments': comments,
                'liked': liked,
            }
        )


class AddCarPost(View):
    """
    To add a post 
    """

    def get(self, request, *args, **kwargs):
        """
        To view AddCarForm in add_car.html
        """
        form = AddCarForm(request.POST)
        context = {
            'cars': 'active',
            'form': form,
        }
        return render(request, 'cars/add_car.html', context)

    def post(self, request, *args, **kwargs):
        """ 
        To post
        """
        if request.method == "POST":
            form = AddCarForm(request.POST, request.FILES)
            
            if form.is_valid():
                car_post = PostCar()
                car_post.car_model_title = request.POST.get('car_model_title')
                car_post.year_manufactured = request.POST.get('year_manufactured')
                car_post.author = request.user
                car_post.content = request.POST.get('content')
                car_post.car_image = request.FILES.get('car_image')
                car_post.status = request.POST.get('status')
                car_post.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Your car is posted successfully. Thank you for sharing!"
                )
                return redirect('user_profile')
        else:
            form = AddCarForm()

        context = {
            'form': form
        }
        return render(request, 'cars/add_car.html', context)


class EditCarPost(View):
    """
    Edit post
    """
    def get(self, request, post_id, *args, **kwargs):
        """
        To view an specific post
        """
        queryset = PostCar.objects.filter(status=1)
        post_car = get_object_or_404(queryset, pk=post_id)
        edit_car = AddCarForm(request.POST or None, instance=post_car)
        context = {
            'form': edit_car,
            'cars': 'active',
        }
        return render(request, 'cars/edit_car.html', context)

    def post(self, request, post_id, *args, **kwargs):
        """
        to post
        """
        queryset = PostCar.objects.filter(status=1)
        post_car = get_object_or_404(queryset, pk=post_id)
        edit_car = AddCarForm(request.POST or None, request.FILES or None, instance=post_car)
        if edit_car.is_valid():
            post_car.date_created = post_car.date_updated
            edit_car.save()
            return redirect('car_detail', str(post_id))
        context = {
            'form': edit_car,
            'cars': 'active',
            'post_car.date_created': post_car.date_updated,
        }
        return render(request, 'cars/edit_car.html', context)


class DeleteCarPost(View):
    """
    Delete view
    """
    def get(self, request, post_id, *args, **kwargs):
        """
        Get the post
        """
        queryset = PostCar.objects.filter(status=1)
        post_car = get_object_or_404(queryset, pk=post_id)
        post_car.delete()
        return redirect('user_profile')
