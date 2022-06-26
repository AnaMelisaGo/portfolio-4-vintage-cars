from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Event
from .forms import EventForm


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


class AddEventView(generic.CreateView):
    """
    A view class to add new event post, only available for staff
    """
    def get(self, request, *args, **kwargs):
        """
        To view EventForm in add_event.html, and pass context to template
        to be used to create a post
        """
        form = EventForm(request.POST)
        context = {
            'events': 'active',
            'form': form,
        }
        return render(request, 'cars/add_car.html', context)

    def post(self, request, *args, **kwargs):
        """
        To post an event if form is valid
        """
        if request.method == "POST":
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                event = Event()
                event.event_title = request.POST.get('event_title')
                event.location = request.POST.get('location')
                event.author = request.user
                event.content = request.POST.get('content')
                event.event_image = request.FILES.get('event_image')
                event.event_excerpt = request.POST.get('event_excerpt')
                event.event_date = request.POST.get('event_date')
                event.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Event is successfully posted. Thank you for sharing!"
                )
                return redirect('events')
        else:
            form = EventForm()

        context = {
            'form': form
        }
        return render(request, 'events/add_event.html', context)


class EditEventView(generic.UpdateView):
    """
    To update event post
    """
    def get(self, request, pk, *args, **kwargs):
        """
        To get the form to be edited
        """
        event = get_object_or_404(Event, pk=pk)
        edit_event = EventForm(
            request.POST or None, request.FILES or None, instance=event
        )
        context = {
            'form': edit_event,
            'events': 'active',
        }
        return render(request, 'cars/edit_car.html', context)

    def post(self, request, pk, *args, **kwargs):
        """
        Takes the content of the event post and put them on each field. Request.FILES
        or None is used to get media files to be posted.
        """
        event = get_object_or_404(Event, pk=pk)
        edit_event = EventForm(
            request.POST or None, request.FILES or None, instance=event
        )
        if edit_event.is_valid():
            edit_event.save()
            messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Your car is modified successfully!"
                )
            return redirect('events')
        context = {
            'form': edit_event,
            'events': 'active',
        }
        return render(request, 'cars/edit_car.html', context)
