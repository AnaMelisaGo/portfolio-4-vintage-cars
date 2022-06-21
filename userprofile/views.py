from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages
from django.urls import reverse_lazy
from cars.models import PostCar
from .filters import PostCarFilter


class UserProfileView(View):
    """ Show user profile """
    def get(self, request):
        """ render user profile """
        post_car = PostCar.objects.order_by('-date_created')

        car_filter = PostCarFilter(request.GET, queryset=post_car)
        post_car = car_filter.qs

        context = {
            'user_profile': 'active',
            'post_car': post_car,
            'car_filter': car_filter,
        }
        return render(request, 'registration/user_profile.html', context)


class UserRegisterView(generic.CreateView):
    """
    To create a new user
    """
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_message = "%(name)s was created successfully"
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        """ insert context """
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        context['user_profile'] = 'active'
        return context


def logout_message(sender, user, request, **kwargs):
    """ show message """
    messages.add_message(
        request,
        messages.WARNING,
        'You successfully logged out. See you soon again!'
    )


def login_message(sender, user, request, **kwargs):
    """ show message """
    messages.add_message(
        request,
        messages.SUCCESS,
        'Welcome! You are logged in to your account.'
    )


user_logged_out.connect(logout_message)
user_logged_in.connect(login_message)
