from django.db import models

# Create your models here.
class Orders(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    status = models.CharField(max_length=200)