# Generated by Django 4.1.3 on 2023-01-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0022_alter_artwork_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artwork",
            name="topic",
            field=models.TextField(
                blank=True, default="I would like feedback on these topics:", null=True
            ),
        ),
    ]