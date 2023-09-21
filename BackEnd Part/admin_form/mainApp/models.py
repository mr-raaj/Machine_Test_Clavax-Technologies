from django.db import models

# Create your models here.

# app_name/models.py
from django.db import models

class ClassDetail(models.Model):
    class_name = models.CharField(max_length=100)
    
