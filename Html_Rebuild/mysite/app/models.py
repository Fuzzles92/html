from django.db import models

class Input(models.Model):
    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)