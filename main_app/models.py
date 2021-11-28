from django.db import models
from django.urls import reverse
from datetime import date

TECHNIQUES = (
  ("D", "Dry"),
  ("A", "Alcohol"),
  ("Q", "Q-Tip")
)

# Create your models here.

class Comic(models.Model):
  artist = models.CharField(max_length=25)
  title = models.CharField(max_length=50)
  publisher = models.CharField(max_length=25)
  issue = models.IntegerField()
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('comics_detail', kwargs={'pk': self.id})

class Figure(models.Model):
  name = models.CharField(max_length=25)
  brand = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  scale = models.IntegerField()
  comics = models.ManyToManyField(Comic)

  def __str__(self):
    return self.name
    
  
  def get_absolute_url(self):
    return reverse('figures_detail', kwargs={'figure_id': self.id})

  def clean_for_today(self):
    return self.cleaning_set.filter(date=date.today()).count() >= len(TECHNIQUES)

class Cleaning(models.Model):
  date = models.DateField("Cleaning Date")
  technique = models.CharField(
    max_length=1,
    choices=TECHNIQUES,
    default=TECHNIQUES[0][0]
  )
  figure = models.ForeignKey(Figure, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_technique_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  figure = models.OneToOneField(Figure, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for figure_id: {self.figure_id} @{self.url}"