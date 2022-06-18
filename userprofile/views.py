from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from cars.models import PostCar


class UserProfileView(View):
    """ Show user profile """
    def get(self, request):
        """ render user profile """
        post_car = PostCar.objects.filter(status=1).order_by('-date_created')
        paginator = Paginator(post_car, 6)
        page_number = request.GET.get('page')
        page_car = paginator.get_page(page_number)
        context = {
            'user_profile': 'active',
            'post_car': page_car,
        }
        return render(request, 'registration/user_profile.html', context)


class UserRegisterView(generic.CreateView):
    """
    To create a new user
    """
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        """ insert context """
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        context['user_profile'] = 'active'
        return context
