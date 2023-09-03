from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.updateProfile.as_view(), name='profile'),
    # path('profile/', views.profile, name='profile'),

]
