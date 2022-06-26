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

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['events'] = 'active'
        context['events_post'] = Event.objects.all()
        return context


class EventDetail(generic.DetailView):
    """
    To view the detail of the event
    """
    model = Event
    template_name = "events/event_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['events'] = 'active'
        return context
