from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('cars/', views.CarPageView.as_view(), name='cars'),
    path('car_detail/<int:post_id>', views.CarDetail.as_view(
    ), name='car_detail'),
]
