from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name =  models.CharField(max_length = 20)
    comment =   models.TextField(max_length = 255)
    date_added  = models.DateTimeField( default=timezone.now)  
