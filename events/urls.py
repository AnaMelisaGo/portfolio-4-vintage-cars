from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventView.as_view(), name='events'),
    path('event_detail/<int:pk>', views.EventDetail.as_view(
    ), name='event_detail'),
]
