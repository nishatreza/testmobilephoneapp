from django.db import models

# Create your models here.


class Mobile(models.Model):
    brand_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    jan_code = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')



