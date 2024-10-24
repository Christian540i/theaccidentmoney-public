# Generated by Django 4.0.5 on 2024-10-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_lead_insured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='commercial_vehicle',
            field=models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='lead',
            name='fracture',
            field=models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='lead',
            name='insured',
            field=models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='lead',
            name='passenger',
            field=models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='lead',
            name='pedestrian',
            field=models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='lead',
            name='rear_end',
            field=models.CharField(choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')], default='', max_length=3),
        ),
    ]