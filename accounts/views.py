from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserUpdateForm
from django.views import View


# Create your views here.

def signin(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        print(user)
        login(request, user)
        return redirect('profile')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

class updateProfile(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    

def profile(request):
    
    return render(request, 'profile.html')