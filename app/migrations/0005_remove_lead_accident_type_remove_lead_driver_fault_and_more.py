# Generated by Django 4.0.5 on 2024-10-23 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_lead_commercial_vehicle_alter_lead_fracture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='accident_type',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='driver_fault',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='injury_severity',
        ),
    ]
