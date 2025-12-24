from django.contrib import admin
from django.urls import path
from caloryapp.views import *

    
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('', indexView, name='home'),
    path('profile/', profileView, name='profile'), 
    path('edit-profile/', editProfileView, name='edit-profile'), 
    path('daily-calory/', consumedCaloryView, name='daily-calory'), 
]
