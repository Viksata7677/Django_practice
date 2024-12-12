from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import NameStartsWithCapital


# Create your models here.


class Profile(models.Model):
    nickname = models.CharField(max_length=20, validators=[MinLengthValidator(2, message="Nickname must be at least 2 chars long!"),], unique=True)
    first_name = models.CharField(max_length=30, validators=[NameStartsWithCapital()])
    last_name = models.CharField(max_length=30, validators=[NameStartsWithCapital()])
    chef = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)