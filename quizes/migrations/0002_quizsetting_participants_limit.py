# Generated by Django 4.2.4 on 2023-08-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsetting',
            name='participants_limit',
            field=models.IntegerField(default=None),
        ),
    ]
