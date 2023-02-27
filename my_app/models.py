from django.db import models

# Create your models here.

class Review(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    stars = models.IntegerField()


class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()