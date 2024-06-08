from django.db import models

# Create your models here.
class carsale(models.Model):
    Brand = models.CharField(max_length=25 ,blank=False, null=True),
    Models = models.CharField(max_length=25, blank=False, null=True)

    def __str__(self):
        return "{self.Brand}: {self.Models}"