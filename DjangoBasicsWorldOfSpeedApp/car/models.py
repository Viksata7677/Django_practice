from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from car.choices import TypeChoices
from car.validators import year_validator
from profiles.models import Profile


# Create your models here.


class Car(models.Model):
    type = models.CharField(max_length=10, choices=TypeChoices.choices)
    model = models.CharField(max_length=15, validators=[MinLengthValidator(1)])
    year = models.IntegerField(validators=[year_validator])
    image_url = models.URLField(unique=True)  # TODO: PLACEHOLDER AND ERROR MESSAGE FOR UNIQUE
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
