# Generated by Django 4.1.3 on 2023-01-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0015_alter_artwork_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artwork",
            name="title",
            field=models.TextField(blank=True, null=True),
        ),
    ]
