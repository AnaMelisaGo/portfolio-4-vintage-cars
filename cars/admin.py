from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PostCar, Comment


@admin.register(PostCar)
class PostCarAdmin(SummernoteModelAdmin):
    """ Use summernote int the content field in admin """
    list_filter = ('status', 'date_created', 'year_manufactured')
    list_display = ('car_model_title', 'status', 'date_created')
    search_fields = ['car_model_title', 'content']
    summernote_fields = ('content')
    actions = ['add_featured_car']

    def add_featured_car(self, request, queryset):
        """ Add a featured car """
        queryset.update(featured_car=True)


admin.site.register(Comment)
