# Generated by Django 2.1.4 on 2019-01-03 19:59

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0001_creating_user_model")]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("hours", models.FloatField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="api.User",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="api.User",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="api.User",
                    ),
                ),
            ],
        )
    ]
