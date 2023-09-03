from django.contrib import admin
from .models import Profile, Skill

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('phone',)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)