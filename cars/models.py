from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


class PostCar(models.Model):
    """
    Create model to post car
    """
    car_model_title = models.CharField(max_length=200)
    year_manufactured = models.IntegerField(
        validators=[MinValueValidator(1875), MaxValueValidator(2000)]
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_cars'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    car_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='like_cars', blank=True
    )
    can_rent = models.BooleanField(default=False)

    class Meta:
        """
        Display post in descending order according to the date
        when the post was created
        """
        ordering = ['-date_created']

    def __str__(self):
        """
        Return car model as title
        """
        return self.car_model_title

    def number_of_likes(self):
        """
        Function to count the number of likes
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Comment model about a car post
    """
    post = models.ForeignKey(
        PostCar, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()

    class Meta:
        """
        Display comments in ascending order according to date
        when comment was created
        """
        ordering = ['date_created']

    def __str__(self):
        """
        Return a string of the comment
        """
        return f'Comment {self.comment_body} by {self.name}'