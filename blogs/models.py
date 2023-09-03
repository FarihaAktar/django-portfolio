from django.db import models

# Create your models here.

status_field = (
    ('Latest', 'Latest'),
    ('New', 'New'),
    ('Old', 'Old'),
)

class Blog(models.Model):
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=500)
    url = models.URLField(max_length=300)
    status = models.CharField(max_length=100, choices=status_field, default='Latest')
    
    
