from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            UsernameValidator(),
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )