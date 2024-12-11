# Generated by Django 5.1.3 on 2024-11-14 13:44

import django.core.validators
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, message='Username must be at least 3 chars long!'), profiles.validators.AlphaNumericValidator()])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(help_text='Age requirement: 21 years and above.', validators=[django.core.validators.MinValueValidator(21)])),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
