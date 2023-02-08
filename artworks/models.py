from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from panelists.models import Profile


class Artwork(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default_image.jpg"
    )
    description = models.TextField(null=True, blank=True)
    topic = models.TextField(default="I would like feedback on:", null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    star_total = models.IntegerField(default=0, null=True, blank=True)
    star_ratio = models.IntegerField(default=0, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-star_ratio", "-star_total", "-vote_ratio", "-vote_total", "title"]
        # Projects display in descending order by value and number of reviews, otherwise by title.

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list("owner__id", flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()

        upVotes = reviews.filter(value="up").count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

    @property
    def getStarCount(self):
        stars = self.star_set.all()
        rating = stars(includes="&#11088; ").count()

        fraction = (rating / stars) * 100
        self.star_total = stars
        self.star_ratio = fraction
        self.save()



class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    VOTE_TYPE = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )
    comments = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    class Star(models.TextChoices):
        one = "&#11088; "
        two = one + one
        three = two + one
        four = three + one
        five = four + one

    stars = models.CharField(
        max_length=50,
        choices=Star.choices,
        default=Star.five,
    )

    def is_rated(self):
        return self.stars in {
            self.stars,
        }

    def __str__(self):
        return self.stars

    def __str__(self):
        return self.value


# Use Tag to create a Many to Many relationship.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name

