from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Event
from .forms import EventForm


class EventListView(generic.ListView):
    """
    View the events
    """
    model = Event
    template_name = 'events/events_list.html'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
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


class AddEventView(PermissionRequiredMixin, generic.CreateView):
    """
    A view class to add new event post, only available for staff
    """
    model = Event
    form_class = EventForm
    permission_required = 'is_staff'
    template_name = 'events/add_event.html'

    def get_context_data(self, **kwargs):
        context = super(AddEventView, self).get_context_data(**kwargs)
        context['events'] = 'active'
        return context

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
            'form': form,
        }
        return render(request, 'events/add_event.html', context)


class EditEventView(PermissionRequiredMixin, View):
    """
    To update event post
    """
    permission_required = 'is_staff'

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
        return render(request, 'events/edit_event.html', context)

    def post(self, request, pk, *args, **kwargs):
        """
        Takes the content of the event post and put them on each field. 
        Request.FILES or None is used to get media files to be posted.
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
                    "Your event is updated successfully!"
                )
            return redirect('events')
        context = {
            'form': edit_event,
            'events': 'active',
        }
        return render(request, 'events/edit_event.html', context)


class DeleteEventView(PermissionRequiredMixin, View):
    """
    To delete an event post
    """
    permission_required = 'is_staff'
    
    def get(self, request, pk, *args, **kwargs):
        """
        A function that deletes the desired object and redirects
        user to user profile page
        """
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        messages.add_message(
                    request,
                    messages.ERROR,
                    "The event is deleted"
                )
        return redirect('events')
