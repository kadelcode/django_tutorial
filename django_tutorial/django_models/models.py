'''
- A model is the single, definitive source of information about your data.
- It contains fields.
- Fields are the most important part of a model. It's the only required part of a model
- Fields are specified by class attributes
- Don't use a field name that conflicts with the models API like clean, save, or delete

'''
from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()