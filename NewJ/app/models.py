from django.db import models

# Create your models here.
class Man(models.Model):
    name = models.TextField(max_length=20)