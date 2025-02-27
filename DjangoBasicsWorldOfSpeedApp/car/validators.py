from django.core.exceptions import ValidationError


def year_validator(value):
    if not (1999 <= value <= 2030):
        raise ValidationError(
            "Year must be between 1999 and 2030!",
            code='invalid_year'
        )