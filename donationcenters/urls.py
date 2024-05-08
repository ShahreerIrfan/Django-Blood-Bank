from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.donors, name='donors'),
    path('request/', views.create_blood_request, name='create_blood_request'),
    path('blood-requests/', views.blood_requests_list, name='blood_requests_list'),
    path('emergency-requests/', views.create_emergency_blood_request, name='emergency_requests'),
    path('blood-requests/edit/<int:pk>/', views.edit_blood_request, name='edit_blood_request'),
    path('blood-requests/delete/<int:pk>/', views.delete_blood_request, name='delete_blood_request'),
    path('blood-requests/<int:pk>/', views.blood_request_details, name='blood_request_details'),
    path('complete_blood_donation/<int:pk>/', views.complete_blood_donation, name='complete_blood_donation'),
    path('complete_blood_donation_details_page/<int:pk>/', views.complete_blood_donation_details, name='complete_blood_donation_details'),
    path('emergency-blood-requests-list/', views.emergency_blood_requests_list, name='emergency-blood-requests-list'),
    path('emergency-blood-requests-details/<int:pk>/', views.emergency_blood_request_details, name='emergency-blood-details'),

]
