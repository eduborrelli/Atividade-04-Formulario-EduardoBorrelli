from django.db import models

class Top15(models.Model):
  team = models.CharField(max_length=50)
  place = models.CharField(max_length=30)
  fuel = models.CharField(max_length=20)
  placement = models.IntegerField()

class common_sectors(models.Model):
  IMPORTANCE =[
    ("V", "Very important"),
    ("I", "Important"),
    ("N", "Necessary"),
  ]
  DIFFICULTY = [
    ("H", "Hard"),
    ("M", "Medium"),
    ("E", "Easy"),
  ]
  sector = models.CharField(max_length=50)
  priority = models.IntegerField()
  importance = models.CharField(max_length=1, choices=IMPORTANCE)
  difficulty = models.CharField(max_length=1, choices=DIFFICULTY)


  
  