from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Musician


def  musician_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Musician.objects.create(
            user = instance,
            first_name = instance.username,
        )
        print('profile created')


post_save.connect(musician_profile, sender = User)

