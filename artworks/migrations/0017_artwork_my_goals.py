# Generated by Django 4.1.3 on 2023-01-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0016_alter_artwork_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="artwork",
            name="my_goals",
            field=models.TextField(blank=True, null=True),
        ),
    ]
