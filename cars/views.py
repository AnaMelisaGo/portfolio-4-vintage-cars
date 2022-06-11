from django.shortcuts import render
from django.views import View


class HomePageView(View):
    """ view home page """
    def get(self, request, *args, **kwargs):
        """ return homepage """
        context = {
            'home': 'active'
        }
        return render(request, 'home/index.html', context)
