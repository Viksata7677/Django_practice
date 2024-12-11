from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


def validate_password(password):
    if len(password) != 6:
        raise ValidationError("Your passcode must be exactly 6 digits!")


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")


class Author(models.Model):
    first_name = models.CharField(max_length=40, validators=[MinLengthValidator(4), validate_letters_only])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2), validate_letters_only])
    passcode = models.CharField(max_length=6, validators=[validate_password], help_text="Your passcode must be a combination of 6 digits")
    pets_number = models.SmallIntegerField()
    info = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)