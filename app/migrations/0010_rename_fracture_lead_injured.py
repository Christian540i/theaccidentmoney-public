# Generated by Django 4.0.5 on 2024-10-31 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_lead_language_spoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='fracture',
            new_name='injured',
        ),
    ]
