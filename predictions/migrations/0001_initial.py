# Generated by Django 3.0.2 on 2020-01-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
