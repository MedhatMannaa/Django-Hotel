from django.db import models
from django.utils import timezone

# Create your models here.


POST_TYPE =(
    ('DRAFT','DRAFT'),
    ('PUBLISHED','PUBLISHED'),
)

class Post(models.Model): # db table
    title = models.CharField(max_length = 50, unique=True) # column
    content = models.TextField(max_length = 2000, blank=True, null=True) # column
    create_at = models.DateTimeField(default=timezone.now) # column
    active = models.BooleanField(default=False) # column
    author_mail = models.EmailField(default='') # column
    type = models.CharField(choices=POST_TYPE, max_length=30, default='DRAFT') # column
    image = models.ImageField(upload_to='post/')
    
    
    
    
    
    

    def __str__(self):
        return self.title
    