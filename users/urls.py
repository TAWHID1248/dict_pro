from django.urls import path, include
from . import views

app_name = 'users'



urlpatterns = [

 # Include default auth urls.
path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ... other urls

]