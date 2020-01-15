from django.db import models

class Prediction(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    result = models.FloatField(default=0)
