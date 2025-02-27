# Generated by Django 5.1.3 on 2024-11-12 15:48

import author.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), author.models.validate_letters_only])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), author.models.validate_letters_only])),
                ('passcode', models.CharField(help_text='Your passcode must be a combination of 6 digits', max_length=6, validators=[author.models.validate_password])),
                ('pets_number', models.SmallIntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
