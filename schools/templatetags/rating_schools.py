# -*- coding: utf-8 -*-
from django import template

from django.conf import settings

from django.db.models import Sum

from clients.models import Ratings, IsRecomended

register = template.Library()


@register.assignment_tag
def rating_school(school, type_of_rating):
    stars = Ratings.objects.filter(
        school_id=school,
        type_of_rating=type_of_rating
    ).aggregate(stars=Sum("stars"))

    total_votes = Ratings.objects.filter(
        school_id=school,
        type_of_rating=type_of_rating
    ).count()

    maximum_stars = settings.NUMBER_OF_STARS

    stars = 0 if stars["stars"] is None else stars["stars"]

    total_votes = 1 if total_votes == 0 else total_votes

    total_stars = stars / (float(total_votes * maximum_stars)) * maximum_stars

    return total_stars


@register.assignment_tag
def comments_about_rating(school, type_of_rating):
    return Ratings.objects.filter(
        school_id=school,
        type_of_rating=type_of_rating
    )


@register.assignment_tag
def total_raitings_in_the_school(school):
    return Ratings.objects.filter(
        school_id=school
    ).count()


@register.assignment_tag
def exists_recomendation(school, user):
    return IsRecomended.objects.filter(
        school_id=school,
        user=user
    ).values("type_of_rating")


@register.assignment_tag
def recomends_percentages(school):
    total_users = IsRecomended.objects.filter(
        school_id=school
    ).count()

    if total_users == 0:
        total_users = 1
        total_recomend = 0
        total_may_recomend = 0
        total_not_recomend = 0

    else:

        total_recomend = IsRecomended.objects.filter(
            school_id=school,
            type_of_rating="i_recomend"
        ).count()

        total_may_recomend = IsRecomended.objects.filter(
            school_id=school,
            type_of_rating="i_do_not_know_if_i_recomend"
        ).count()

        total_not_recomend = IsRecomended.objects.filter(
            school_id=school,
            type_of_rating="i_do_not_recomend"
        ).count()

    percentage_recomend = float(total_recomend / float(total_users)) * 100
    percentage_may_recomend = float(total_may_recomend / float(total_users)) * 100
    percentagem_not_recomend = float(total_not_recomend / float(total_users)) * 100

    return {
        "perc_recomendations": "%.2f" % percentage_recomend,
        "perc_may_recomend": "%.2f" % percentage_may_recomend,
        "perc_not_recomend": "%.2f" % percentagem_not_recomend,
        "total_reviews": total_users,
        "total_recomend": total_recomend,
        "total_may_recomend": total_may_recomend,
        "total_not_recomend": total_not_recomend
    }
