from django.db import models
from PIL import Image
from django.db import connection

# Create your models here.

class carsale(models.Model):
    model = models.CharField(max_length=25, blank=True, null=False)
    brand = models.CharField(max_length=25, blank=True, null=False)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Image is being created
            super().save(*args, **kwargs)
            img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        else:  # Image is being updated
            super().save(*args, **kwargs)


    class Meta:
        db_table = "carsales"
