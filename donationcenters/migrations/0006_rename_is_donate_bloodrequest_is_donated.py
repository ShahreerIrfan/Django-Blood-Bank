# Generated by Django 5.0.1 on 2024-04-23 23:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "donationcenters",
            "0005_bloodrequest_created_at_alter_bloodrequest_is_donate",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="bloodrequest",
            old_name="is_donate",
            new_name="is_donated",
        ),
    ]
