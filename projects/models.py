from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.category_name
    
Choice_field = (
        (1, 'React'),
        (2, 'Javascript'),
        (3, 'Android'),
        (4, 'Django'),
        (5, 'Bootstrap-5'),
        (6, 'Custom-CSS'),
        (7, 'Jquery'),
        (8, 'Node'),
    )
    
class Project(models.Model):
    project_title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    screenshot = models.ImageField(upload_to='photos/projects')
    project_url = models.URLField(max_length=300)
    technologies_used = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    

class ReviewRating(models.Model):
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    viewer_name = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    rating = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)