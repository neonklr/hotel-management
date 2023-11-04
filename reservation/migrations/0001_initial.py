# Generated by Django 4.2.6 on 2023-11-04 03:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "room_no",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("room_type", models.CharField(max_length=100)),
                ("room_price", models.IntegerField()),
                ("is_available", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date", models.DateField()),
                ("booked_from", models.DateTimeField()),
                ("booked_to", models.DateTimeField()),
                ("payment_method", models.CharField(max_length=20)),
                ("payment_amount", models.IntegerField()),
                ("checked_out_at", models.DateTimeField(blank=True, null=True)),
                ("completed", models.CharField(max_length=100)),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
                (
                    "room_no",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservation.room",
                    ),
                ),
            ],
        ),
    ]
