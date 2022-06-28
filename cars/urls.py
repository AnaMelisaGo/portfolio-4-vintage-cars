from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('car_lists/', views.CarPageView.as_view(), name='cars'),
    path('car_detail/<int:post_id>', views.CarDetail.as_view(
    ), name='car_detail'),
    path('add_car/', login_required(views.AddCarPost.as_view(
    )), name='add_car'),
    path('edit_car/<int:post_id>', login_required(views.EditCarPost.as_view(
    )), name='edit_car'),
    path('delete_car/<int:post_id>', login_required(
        views.DeleteCarPost.as_view()
    ), name='delete_car'),
    path('like/<int:post_id>', login_required(views.LikeCar.as_view(
    )), name='like_car'),
]
