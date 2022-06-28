from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('event_list/', views.EventListView.as_view(), name='events'),
    path('event_detail/<int:pk>', views.EventDetail.as_view(
    ), name='event_detail'),
    path('add_event/', login_required(views.AddEventView.as_view()), name='add_event'),
    path('edit_event/<int:pk>', login_required(views.EditEventView.as_view(
    )), name='edit_event'),
    path('delete_event/<int:pk>', login_required(views.DeleteEventView.as_view(
    )), name='delete_event'),
]
