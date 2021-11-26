from django.db import models
from django.urls import reverse

CLEANS = (
  ("D", "Dry"),
  ("A", "Alcohol"),
  ("Q", "Q-Tip")
)

# Create your models here.

class Figure(models.Model):
  name = models.CharField(max_length=25)
  brand = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  scale = models.IntegerField()

  def __str__(self):
    return self.name
    
  
  def get_absolute_url(self):
    return reverse('figures_details', kwargs={'figure_id': self.id})

class Cleaning(models.Model):
  date = models.DateField("Cleaning Date")
  clean = models.CharField(
    max_length=1,
    choices=CLEANS,
    default=CLEANS[0][0]
  )
  figure = models.ForeignKey(Figure, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_clean_display()} on {self.date}"