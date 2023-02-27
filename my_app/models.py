from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Review(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])