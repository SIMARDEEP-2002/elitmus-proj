# Generated by Django 4.0.2 on 2023-05-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_alter_team_level1_alter_team_level2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
