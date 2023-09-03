from django.contrib import admin
from .models import Category, Project, ReviewRating

# Register your models here.

class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ('category_name', 'slug')
    
    
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('project_title',)}
    list_display = ('project_title', 'slug', 'technologies_used')
    
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('viewer_name', 'rating', 'status', 'created_at')
    
admin.site.register(Category, ProjectCategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
