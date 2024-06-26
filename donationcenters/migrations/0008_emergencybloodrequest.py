# Generated by Django 5.0.4 on 2024-04-26 09:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("donationcenters", "0007_rename_is_donated_bloodrequest_is_donate"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmergencyBloodRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "blood_group",
                    models.CharField(
                        choices=[
                            ("A+", "A+"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B-", "B-"),
                            ("O+", "O+"),
                            ("O-", "O-"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "why_need",
                    models.CharField(
                        choices=[
                            ("Oxygen Delivery", "Oxygen Delivery"),
                            ("Clotting", "Clotting"),
                            ("Nutrient Transport", "Nutrient Transport"),
                            ("Waste Removal", "Waste Removal"),
                            ("Immune Response", "Immune Response"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("where_need", models.CharField(max_length=200, null=True)),
                ("donation_date", models.DateTimeField(null=True)),
                (
                    "blood_quantity",
                    models.CharField(
                        choices=[
                            ("1 Bag", "1 Bag"),
                            ("2 Bags", "2 Bags"),
                            ("3 Bags", "3 Bags"),
                            ("4 Bags", "4 Bags"),
                            ("5 Bags", "5 Bags"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "hemoglobin_level",
                    models.CharField(
                        choices=[
                            ("1", 1),
                            ("2", 2),
                            ("3", 3),
                            ("4", 4),
                            ("5", 5),
                            ("6", 6),
                            ("7", 7),
                            ("8", 8),
                            ("9", 9),
                            ("10", 10),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("hospital_name", models.CharField(max_length=200, null=True)),
                ("phone_number", models.CharField(max_length=20, null=True)),
                ("additional_information", models.TextField(null=True)),
                ("is_donate", models.BooleanField(default=False, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "requester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
