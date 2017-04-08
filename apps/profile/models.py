from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..utils.countries import COUNTRIES
from ..utils.gender import GENDERS


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    nationality = models.CharField(max_length=2, choices=COUNTRIES)
    gender = models.CharField(max_length=1, choices=GENDERS)
    birth_day = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
