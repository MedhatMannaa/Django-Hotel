from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model): # db table
    title = models.CharField(max_length = 50) # column
    content = models.TextField(max_length = 2000) # column
    create_at = models.DateTimeField(default=timezone.now)
    
    
    

def __str__(self):
    return self.title
    