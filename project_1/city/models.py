from django.db import models

# Create your models here.
class City(models.Model):
    city_tital = models.CharField(max_length=50)
    city_description = models.TextField()
