# Generated by Django 4.1.3 on 2023-02-12 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("panelists", "0011_message"),
        ("artworks", "0029_alter_review_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("owner", "artwork")},
        ),
    ]
