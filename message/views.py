from django.shortcuts import render, redirect
from .forms import MessageForm

# Create your views here.
def add_message(request):  
    print(request.POST)
    if request.method == 'POST':
        try:
            form = MessageForm(request.POST)
            review = form.save(commit=False)
            res = review.save()
            print(res)
            return redirect('home')
            # return render(request, 'project_detail')
        except ValueError:
            return redirect('home')  
    else:      
        return render(request, 'home')  
