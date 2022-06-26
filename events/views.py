from django.shortcuts import render
from django.views import generic
from .models import Event


# def event_view(request):
#     return render(request, 'events/events.html', {})

class EventView(generic.ListView):
    """
    View the events
    """
    model = Event
    template_name = 'events/events_list.html'
