import os
from django.shortcuts import render
from django.views import View


class HomePageView(View):
    """
    To view home page so any user can access the 
    different pages of the website
    """

    def get(self, request):
        """ return homepage """
        context = {
            'home': 'active'
        }
        return render(request, 'home/index.html', context)


class ContactPage(View):
    """
    To display the contact page
    """
    def get(self, request):
        """
        To render the contact page and show contents
        """
        context = {
            'contact': 'active',
            'USER_ID': os.environ.get('USER_ID'),
        }
        return render(request, 'home/contact.html', context)


def handle_404_error(request, exception):
    """
    Display custom 400.html template to user
    when 404 error is detected
    """
    return render(request, '404.html')


def handle_500_error(request):
    """
    Display custom 500.html template to user
    when 500 error is detected
    """
    return render(request, '500.html')
