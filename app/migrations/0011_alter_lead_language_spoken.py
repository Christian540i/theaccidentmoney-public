# Generated by Django 4.0.5 on 2024-10-31 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_fracture_lead_injured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='language_spoken',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
