from django.db import models
import uuid
from panelists.models import Profile


class Artwork(models.Model):
    critic = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.RESTRICT
    )
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(
        null=True, blank=True, default="default_image.jpg"
    )
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ("poor", 1),
        ("fair", 2),
        ("good", 3),
        ("excellent", 4),
        ("sublime", 5),
    )
    # owner =
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.value


# Use Tag to create a Many to Many relationship. It connects the Artworks with the votes they receive.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name
