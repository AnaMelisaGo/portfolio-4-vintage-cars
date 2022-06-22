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
            'contact': 'active'
        }
        return render(request, 'home/contact.html', context)
