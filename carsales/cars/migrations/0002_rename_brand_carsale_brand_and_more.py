# Generated by Django 5.0.6 on 2024-06-10 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carsale',
            old_name='Brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='carsale',
            old_name='Model',
            new_name='model',
        ),
    ]
