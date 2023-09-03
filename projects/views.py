from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, ReviewRating
from .forms import ReviewForm

# Create your views here.

def projects(request):
    return render(request, 'projects.html')


def project_detail(request, project_slug):
    single_project = Project.objects.get(slug = project_slug)
    reviews = ReviewRating.objects.filter(project=single_project, status = True)
    return render(request, 'project_detail.html', {'project' : single_project, 'reviews': reviews})



def submit_review(request,project_slug):   
    print(project_slug)
    print('post',request.POST)
    if request.method == 'POST':
        
        try:
            project = get_object_or_404(Project, slug = project_slug)
            print('project------',project)
            form = ReviewForm(request.POST)
            review = form.save(commit=False)
            review.project = project
            review.save()
            
            return redirect('project_detail', project_slug)
            # return render(request, 'project_detail')
        except ValueError:
            print("helow world")
            return redirect('project_detail', project_slug)  
    else:      
        return redirect('project_detail', project_slug)    