# Generated by Django 4.0.2 on 2022-06-29 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_participant_phoneno_alter_participant_rollno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='discord_ID',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Enter a valid discord ID', regex='^.{2,32}#[0-9]{4}$')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='board',
            field=models.IntegerField(default=0),
        ),
    ]
