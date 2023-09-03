from django.db import models

# Create your models here.
SERVICE = (
    ('Websites', 'Websites'),
    ('Branding', 'Branding'),
    ('Ecommerce', 'Ecommerce'),
    ('SEO', 'SEO'),
)
class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    service = models.CharField(max_length=100, choices=SERVICE)