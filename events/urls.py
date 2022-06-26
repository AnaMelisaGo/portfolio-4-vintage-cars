from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventView.as_view(), name='events'),
    path('event_detail/<int:pk>', views.EventDetail.as_view(
    ), name='event_detail'),
    path('add_event/', views.AddEventView.as_view(), name='add_event'),
    path('event/edit/<int:pk>', views.EditEventView.as_view(
    ), name='edit_event'),
    path('event/delete/<int:pk>', views.DeleteEventView.as_view(
    ), name='delete_event'),
]
