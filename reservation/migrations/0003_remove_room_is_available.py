# Generated by Django 4.2.6 on 2023-11-04 06:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reservation", "0002_rename_date_reservation_booked_on_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="is_available",
        ),
    ]