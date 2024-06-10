from django.db import models
from PIL import Image
from django.db import connection

# Create your models here.

class carsale(models.Model):
    model = models.CharField(max_length=25, blank=True, null=False)
    brand = models.CharField(max_length=25, blank=True, null=False)

    
    class Meta:
        db_table = "carsales"
