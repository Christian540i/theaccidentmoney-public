# Generated by Django 4.0.5 on 2024-10-31 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_lead_commercial_vehicle_alter_lead_fracture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='language_spoken',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
