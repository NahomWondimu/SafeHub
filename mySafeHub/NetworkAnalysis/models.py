from django.db import models

# Create your models here.
class Network(models.Model):
    placeHolder = models.CharField(max_length=255)
    time_entered = models.TimeField(null=True)