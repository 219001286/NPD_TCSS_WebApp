from django.db import models

# table for vehicles 

# class Vehicles (models.Model):
#     vehicle_category = models.


class Categories (models.Model):
    name = models.CharField(max_length=80)
    registered_time = models.DateField()