# -*- coding: utf-8 -*-
from django import template

from schools.models import School, SchoolFeed
register = template.Library()


@register.assignment_tag
def list_school():
    results = []
    schools = School.objects.all()

    for obj in schools:
        try:
            results.append({
                "school": obj.name,
                "image": "static/{}".format(obj.logo_image.path.split("/")[-1:][0]),
                "id": obj.pk
            })
        except ValueError:
            results.append({
                "school": obj.name,
                "image": "static/not_found.jpg",
                "id": obj.pk
            })
    return results


@register.assignment_tag
def feed_school():
    return SchoolFeed.objects.all()
