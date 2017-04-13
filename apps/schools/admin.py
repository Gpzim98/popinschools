from django.contrib import admin
from .models import (
    School,
    ImageGalery,
    Videos,
    EventsOffered,
    Accommodation,
    Languages,
    Ratings,
    Course,
    Comment
)


class ImageInline(admin.TabularInline):
    model = ImageGalery
    extra = 1


class VideoInline(admin.TabularInline):
    model = Videos
    extra = 1


class SchoolAdmin(admin.ModelAdmin):
    inlines = (ImageInline, VideoInline)
    list_display = ('id', 'name', 'ratings')
    list_filter = ('id', 'name')
    ordering = ('id', 'name')
    search_fields = ('id', 'name')
    filter_horizontal = []


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'approved')
    search_fields = ('user', 'school', 'approved')
    list_filter = ('approved', )

admin.site.register(School, SchoolAdmin)
admin.site.register(ImageGalery)
admin.site.register(EventsOffered)
admin.site.register(Videos)
admin.site.register(Accommodation)
admin.site.register(Languages)
admin.site.register(Ratings)
admin.site.register(Course)
admin.site.register(Comment, CommentAdmin)
