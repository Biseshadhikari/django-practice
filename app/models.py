from django.db import models

# Create your models here.

class Todolist(models.Model): 
    title = models.CharField(max_length=255)
    days = models.IntegerField()
    is_completed = models.BooleanField()
    
    