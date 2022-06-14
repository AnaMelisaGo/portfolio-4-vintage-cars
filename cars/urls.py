from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('cars/', views.CarPageView.as_view(), name='cars')
]
