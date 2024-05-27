from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.tools, name='tools'),
    path('bmi/', views.calculateBMI, name='bmi'),
    
]