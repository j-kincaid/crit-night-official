# Generated by Django 4.1.3 on 2023-02-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panelists", "0012_alter_profile_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="role",
            field=models.CharField(
                choices=[("moderator", "Moderator"), ("artist", "Artist")],
                max_length=200,
                null=True,
            ),
        ),
    ]
