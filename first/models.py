from django.db import models

# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'carmodel'
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.IntegerField()
    year = models.IntegerField()