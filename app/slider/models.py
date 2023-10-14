from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, default='')
    url = models.ImageField(upload_to='asset/images/sliders')
    
    def  __str__(self):
        return self.title