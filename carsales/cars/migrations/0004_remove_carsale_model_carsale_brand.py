# Generated by Django 5.0.6 on 2024-06-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_carsale_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carsale',
            name='Model',
        ),
        migrations.AddField(
            model_name='carsale',
            name='Brand',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
