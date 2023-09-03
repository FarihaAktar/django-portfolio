from django.db import models
from projects.models import Project
from blogs.models import Blog


# Create your models here.

class Skill(models.Model):
    name= models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class Profile(models.Model):
    image = models.ImageField(upload_to='photos/self')
    phone = models.IntegerField()
    skill = models.ManyToManyField(Skill)
    
    

    
