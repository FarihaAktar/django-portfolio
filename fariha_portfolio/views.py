from django.shortcuts import render
from projects.models import Project
from blogs.models import Blog
from accounts.models import Profile, Skill


# Create your views here.

def home(request):
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    profile = Profile.objects.all()
    skill = Skill.objects.all()
    print(projects)
    return render(request, 'base.html', {'projects': projects, 'blogs': blogs, 'profile': profile, 'skills':skill})