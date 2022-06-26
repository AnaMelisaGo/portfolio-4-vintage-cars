from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator
from cloudinary.forms import cl_init_js_callbacks
from .models import PostCar, Comment
from .forms import AddCarForm, CommentForm
from .filters import PostCarFilter


class CarPageView(View):
    """ Render the list of posted cars and display them to any user
        and separate the posts in pages, limiting the number of car posts in 6
        in each page """
    def get(self, request, *args, **kwargs):
        """ return cars page """
        post_car = PostCar.objects.filter(status=1).order_by('-date_created')
        # filter
        car_filter = PostCarFilter(request.GET, queryset=post_car)
        post_car = car_filter.qs

        # paginator
        paginator = Paginator(post_car, 6)
        page_number = request.GET.get('page')
        page_car = paginator.get_page(page_number)
        context = {
            'cars': 'active',
            'post_car': page_car,
            'car_filter': car_filter,
        }
        return render(request, 'cars/cars.html', context)


class CarDetail(View):
    """
    To view the post's page. It displays the photo,
    content, author and date created
    """
    def get(self, request, post_id, *args, **kwargs):
        """ docstring """
        post_car = get_object_or_404(PostCar, pk=post_id)
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

    def post(self, request, post_id, *args, **kwargs):
        """
        To handle comments on post
        """
        queryset = PostCar.objects.filter(status=1)
        post_car = get_object_or_404(queryset, pk=post_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_post = Comment()
            comment_post.name = request.user.username
            comment_post.comment_body = request.POST.get('comment_body')
            comment_post.post = post_car
            comment_post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your comment is posted."
            )
            return HttpResponseRedirect(reverse('car_detail', args=[post_id]))
        else:
            comment_form = CommentForm()
        context = {
            'cars': 'active',
        }
        return render(request, "car_detail.html", context)


class LikeCar(View):
    """
    Class to get likes from user
    """
    def post(self, request, post_id):
        """
        A funtion to toggle like and unlike when user click on the
        like button
        """
        post_car = get_object_or_404(PostCar, pk=post_id)
        if post_car.likes.filter(id=request.user.id).exists():
            post_car.likes.remove(request.user)
            messages.add_message(
                request,
                messages.ERROR,
                "You unlike the car."
            )
        else:
            post_car.likes.add(request.user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "You like the car."
            )
        return HttpResponseRedirect(reverse('car_detail', args=[post_id]))


class AddCarPost(View):
    """
    To create a post
    """

    def get(self, request, *args, **kwargs):
        """
        To view AddCarForm in add_car.html, and pass context to template
        to be used to create a post
        """
        form = AddCarForm(request.POST)
        context = {
            'cars': 'active',
            'form': form,
        }
        return render(request, 'cars/add_car.html', context)

    def post(self, request, *args, **kwargs):
        """
        If the form is valid, this function will get the value of each
        field. Saves the form to post it and redirects user to user profile
        page.
        """
        if request.method == "POST":
            form = AddCarForm(request.POST, request.FILES)
            if form.is_valid():
                car_post = PostCar()
                car_post.car_model_title = request.POST.get('car_model_title')
                car_post.year_manufactured = request.POST.get(
                    'year_manufactured'
                )
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
    Edit post view
    """
    def get(self, request, post_id, *args, **kwargs):
        """
        To view an specific post that the user wants to edit
        """
        post_car = get_object_or_404(PostCar, pk=post_id)
        edit_car = AddCarForm(
            request.POST or None, request.FILES or None, instance=post_car
        )
        context = {
            'form': edit_car,
            'cars': 'active',
        }
        return render(request, 'cars/edit_car.html', context)

    def post(self, request, post_id, *args, **kwargs):
        """
        Takes the content of the post and put them on each field. Request.FILES
        or None is used to get media files to be posted. Change the value of
        date_created to date_updated when performed any modification
        """
        post_car = get_object_or_404(PostCar, pk=post_id)
        edit_car = AddCarForm(
            request.POST or None, request.FILES or None, instance=post_car
        )
        if edit_car.is_valid():
            edit_car.save()
            post_car.date_created = post_car.date_updated
            messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Your car is modified successfully!"
                )
            return redirect('car_detail', str(post_id))
        context = {
            'form': edit_car,
            'cars': 'active',
        }
        return render(request, 'cars/edit_car.html', context)


class DeleteCarPost(View):
    """
    Class to delete a post
    """
    def get(self, request, post_id, *args, **kwargs):
        """
        A function that deletes the desired object and redirects
        user to user profile page
        """
        post_car = get_object_or_404(PostCar, pk=post_id)
        post_car.delete()
        messages.add_message(
                    request,
                    messages.ERROR,
                    "Your post is deleted"
                )
        return redirect('user_profile')
