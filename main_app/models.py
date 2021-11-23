from django.db import models

# Create your models here.

class Figure(models.Model):
  name = models.CharField(max_length=25)
  brand = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  scale = models.IntegerField()