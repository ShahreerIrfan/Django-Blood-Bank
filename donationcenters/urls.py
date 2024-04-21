from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.donors, name='donors'),
    path('request/', views.create_blood_request, name='create_blood_request'),
]