from django.db.models import TextChoices


class CuisineTypeChoices(TextChoices):
    FRENCH = 'French', 'French'
    CHINESE = 'Chinese', 'Chinese'
    ITALIAN = 'Italian', 'Italian'
    BALKAN = 'Balkan', 'Balkan'
    OTHER = 'Other', 'Other'
