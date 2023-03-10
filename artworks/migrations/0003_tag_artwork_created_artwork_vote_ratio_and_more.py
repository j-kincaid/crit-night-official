# Generated by Django 4.1.3 on 2022-12-06 21:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0002_rename_artwork_title_artwork_title_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="artwork",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="artwork",
            name="vote_ratio",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="artwork",
            name="vote_total",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("body", models.TextField(blank=True, null=True)),
                (
                    "value",
                    models.CharField(
                        choices=[
                            {1, "one star"},
                            {2, "two stars"},
                            {3, "three stars"},
                            {"four stars", 4},
                            {5, "five stars"},
                        ],
                        max_length=200,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "artwork",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="artworks.artwork",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="artwork",
            name="tags",
            field=models.ManyToManyField(blank=True, to="artworks.tag"),
        ),
    ]
