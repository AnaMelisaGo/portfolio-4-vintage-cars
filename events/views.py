from django.contrib import messages
from django.shortcuts import render, redirect
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
    # model = Event
    # template_name = 'events/add_event.html'
    # fields = [
    #     'event_title',
    #     'location',
    #     'event_date',
    #     'event_excerpt',
    #     'content',
    #     'event_image'
    # ]

    def get(self, request, *args, **kwargs):
        """
        To view AddCarForm in add_car.html, and pass context to template
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
        To post
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
                    "Your car is posted successfully. Thank you for sharing!"
                )
                return redirect('events')
        else:
            form = EventForm()

        context = {
            'form': form
        }
        return render(request, 'events/add_event.html', context)

