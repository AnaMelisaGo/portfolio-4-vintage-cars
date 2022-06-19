from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('cars/', views.CarPageView.as_view(), name='cars'),
    path('car_detail/<int:post_id>', views.CarDetail.as_view(
    ), name='car_detail'),
    path('add_car/', views.AddCarPost.as_view(), name='add_car'),
    path('edit_car/<int:post_id>', views.EditCarPost.as_view(), name='edit_car'),
    path('delete_car/<int:post_id>', views.DeleteCarPost.as_view(), name='delete_car')
]
