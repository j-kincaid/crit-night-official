# Generated by Django 4.1.3 on 2023-01-17 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0020_remove_artwork_my_goals_artwork_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artwork",
            name="topic",
            field=models.TextField(
                blank=True, default="My goals for the work are:", null=True
            ),
        ),
    ]
