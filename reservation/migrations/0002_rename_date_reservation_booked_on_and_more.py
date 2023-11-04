# Generated by Django 4.2.6 on 2023-11-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="date",
            new_name="booked_on",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="email",
            new_name="guest",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="room_no",
            new_name="room",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="completed",
            new_name="status",
        ),
        migrations.RenameField(
            model_name="room",
            old_name="room_no",
            new_name="no",
        ),
        migrations.RenameField(
            model_name="room",
            old_name="room_price",
            new_name="price",
        ),
        migrations.RenameField(
            model_name="room",
            old_name="room_type",
            new_name="type",
        ),
        migrations.AddField(
            model_name="reservation",
            name="checked_in_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
