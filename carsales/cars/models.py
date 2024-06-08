from django.db import models

# Create your models here.
class carsale(models.Model):
    Brand = models.CharField(max_length=25, blank=False null=True)
    Models = models.CharField