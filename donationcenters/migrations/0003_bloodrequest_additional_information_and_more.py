# Generated by Django 5.0.1 on 2024-04-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("donationcenters", "0002_remove_bloodrequest_is_fulfilled_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bloodrequest",
            name="additional_information",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="bloodrequest",
            name="hospital_name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="bloodrequest",
            name="phone_number",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
