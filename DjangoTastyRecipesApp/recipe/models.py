from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.models import Profile
from recipe.choices import CuisineTypeChoices


# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(10),], unique=True,
                             error_messages={'unique': "We already have a recipe with the same title!"})
    cuisine_type = models.CharField(max_length=7, choices=CuisineTypeChoices.choices)
    ingredients = models.TextField(help_text="Ingredients must be separated by a comma and space.")
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(validators=[MinValueValidator(1),], help_text="Provide the cooking time in minutes.")
    image_url = models.URLField(null=True, blank=True)
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE)  # TODO: hide in forms
