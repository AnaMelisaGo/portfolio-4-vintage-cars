from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.ContactPage.as_view(), name='contact')
]
