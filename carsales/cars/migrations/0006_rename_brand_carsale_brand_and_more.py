# 0006_rename_brand_carsale_brand_and_more.py
from django.db import migrations, models

class Migration(migrations.Migration):
    operations = [
        migrations.RenameField(
            model_name='carsale',
            old_name='brand',
            new_name='car_brand',
        ),
        migrations.AddField(
            model_name='carsale',
            name='color',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OldModel',
        ),
    ]
