# Generated by Django 3.0.2 on 2020-01-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='result',
            field=models.FloatField(default=0),
        ),
    ]
