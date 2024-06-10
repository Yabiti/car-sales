# Generated by Django 5.0.6 on 2024-06-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='carsale',
            name='Brand',
        ),
        migrations.RemoveField(
            model_name='carsale',
            name='Model',
        ),
        migrations.AlterModelTable(
            name='carsale',
            table='carsales',
        ),
        migrations.AddField(
            model_name='carsale',
            name='brand',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='carsale',
            name='model',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
