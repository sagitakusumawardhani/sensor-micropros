from statistics import mode
from turtle import update
from django.db import models

# Create your models here.
class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    ph = models.FloatField(max_length=4, default=0, null=True)
    tds = models.FloatField(max_length=4, default=0, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)