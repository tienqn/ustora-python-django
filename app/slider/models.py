from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
