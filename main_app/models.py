from django.db import models
from django.urls import reverse

# Create your models here.

class Figure(models.Model):
  name = models.CharField(max_length=25)
  brand = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  scale = models.IntegerField()

  def __str__(self):
    return self.name
    
  
  def get_absolute_url(self):
    return reverse('figures_detail', kwargs={'figure_id': self.id})