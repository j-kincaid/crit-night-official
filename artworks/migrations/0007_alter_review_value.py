# Generated by Django 4.1.3 on 2022-12-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0006_alter_review_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="value",
            field=models.CharField(
                choices=[
                    ("poor", 1),
                    ("fair", 2),
                    ("good", 3),
                    ("excellent", 4),
                    ("sublime", 5),
                ],
                max_length=200,
            ),
        ),
    ]
