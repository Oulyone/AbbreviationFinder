from django.db import models

# Create your models here.
class Abbreviation(models.Model):
    abbreviation = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    project_category = models.CharField(max_length=255)