from django.db import models

class Countries(models.Model):
    country = models.CharField(max_length=50)
    languages = models.CharField(max_length=500)
