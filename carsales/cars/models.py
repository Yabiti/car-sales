from django.db import models

# Create your models here.
class carsale(models.Model):
    Model = models.CharField(max_length=25, blank=True, null=False)
    Brand = models.CharField(max_length=25, blank=True, null=False)


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = "carsale"
