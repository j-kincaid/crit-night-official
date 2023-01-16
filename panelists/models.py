from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import uuid

"""
I should probably have named this app 'users' because I will use it for creating moderator and artist accounts.

"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # models.CASCADE Deletes the profile any time the profile gets deleted
    name = models.CharField(max_length=200, null=True, blank=True)
    media = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    brief_bio = models.TextField(max_length=1200, null=True, blank=True)
    profle_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profiles/",
        default="profiles/default_profile.png",
    )
    website = models.CharField(max_length=200, null=True, blank=True)
    social_insta = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_other = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.user.username)


class Criteria(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.name)


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user


post_save.connect(createProfile, sender=User)


post_delete.connect(deleteUser, sender=Profile)
