from django.contrib import admin
from .models import (
    School,
    ImageGalery,
    Videos,
    EventsOffered,
)


class ImageInline(admin.TabularInline):
    model = ImageGalery
    extra = 1


class VideoInline(admin.TabularInline):
    model = Videos
    extra = 1


class SchoolAdmin(admin.ModelAdmin):
    inlines = (ImageInline, VideoInline)
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id', 'name')
    search_fields = ('id', 'name')
    filter_horizontal = []


admin.site.register(School, SchoolAdmin)
admin.site.register(ImageGalery)
admin.site.register(EventsOffered)
admin.site.register(Videos)
