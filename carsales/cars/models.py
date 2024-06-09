from django.db import models

# Create your models here.
class carsale(models.Model):
    Model = models.CharField(max_length=25, blank=True, null=False)
    Brand = models.CharField(max_length=25, blank=True, null=False)

    class Meta:
        db_table = "carsale"