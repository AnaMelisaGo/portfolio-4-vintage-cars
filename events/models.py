from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Event(models.Model):
    """
    Create model for events
    """
    event_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events'
    )
    event_date = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    event_excerpt = models.TextField(default='Short text about the event')
    content = models.TextField()
    event_image = CloudinaryField('image', default='placeholder')

    class Meta:
        """
        Display post in descending order according to the date
        when the post was created
        """
        ordering = ['-date_created']

    def __str__(self):
        """
        Return event title
        """
        return self.event_title
