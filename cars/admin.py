from django.contrib import admin
from .models import PostCar, Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(PostCar)
admin.site.register(Comment)
