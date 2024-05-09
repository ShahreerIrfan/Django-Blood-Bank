from django.shortcuts import render
from Accounts.models import UserProfile
from django.contrib.auth.models import User
from Accounts.constants import BLOOD_GROUP,GENDER,DISTRICT_CHOICES
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.forms import BLoodRequestForm
from .models import BLoodRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import EmergencyBLoodRequestForm
from .models import EmergencyBloodRequest


def donors(request):
    query = Q()
    blood_group = request.GET.get('blood_group')
    gender = request.GET.get('gender')
    district = request.GET.get('district')

    if blood_group:
        query &= Q(blood_group=blood_group)
    if gender:
        query &= Q(gender=gender)
    if district:
        query &= Q(district=district)

    user_profiles_list = UserProfile.objects.select_related('user').filter(query)
    paginator = Paginator(user_profiles_list, 9)
    page = request.GET.get('page')

    try:
        user_profiles = paginator.page(page)
    except PageNotAnInteger:
        user_profiles = paginator.page(1)
    except EmptyPage:
        user_profiles = paginator.page(paginator.num_pages)

    # Constructing the filter URL..........
    filter_url = reverse('donors') + '?'
    if blood_group:
        filter_url += 'blood_group=' + blood_group + '&'
    if gender:
        filter_url += 'gender=' + gender + '&'
    if district:
        filter_url += 'district=' + district + '&'

    context = {
        'user_profiles': user_profiles,
        'BLOOD_GROUP': BLOOD_GROUP,
        'GENDER': GENDER,
        'DISTRICT_CHOICES': DISTRICT_CHOICES,
        'filter_url': filter_url,
        'blood_group': blood_group,
        'gender': gender,
        'district': district,
    }
    return render(request, 'donationcenters/all_donor.html', context)



@login_required
def create_blood_request(request):
    if request.method == 'POST':
        form = BLoodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.requester = request.user
            blood_request.save()
            return redirect('home')  
    else:
        form = BLoodRequestForm()
    return render(request, 'donationcenters/request_form.html', {'form': form})

def is_admin_user(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

@user_passes_test(is_admin_user, login_url='/login/')  
def blood_requests_list(request):
    blood_requests_list = BLoodRequest.objects.order_by('-created_at')
    paginator = Paginator(blood_requests_list, 5)  

    page_number = request.GET.get('page')
    try:
        blood_requests = paginator.page(page_number)
    except PageNotAnInteger:
        blood_requests = paginator.page(1)
    except EmptyPage:
        blood_requests = paginator.page(paginator.num_pages)

    return render(request, 'donationcenters/blood_requests_list.html', {'blood_requests': blood_requests})
 


def edit_blood_request(request, pk):
    blood_request = get_object_or_404(BLoodRequest, pk=pk)
    if request.method == 'POST':
        form = BLoodRequestForm(request.POST, instance=blood_request)
        if form.is_valid():
            form.save()
            return redirect('blood_requests_list')
    else:
        form = BLoodRequestForm(instance=blood_request)
    return render(request, 'donationcenters/edit_blood_request.html', {'form': form})

def delete_blood_request(request, pk):
    blood_request = get_object_or_404(BLoodRequest, pk=pk)
    if request.method == 'POST':
        blood_request.delete()
    return redirect('blood_requests_list')

def blood_request_details(request, pk):
    blood_request = get_object_or_404(BLoodRequest, pk=pk)
    return render(request, 'donationcenters/blood_request_details.html', {'blood_request': blood_request})

def complete_blood_donation(request, pk):
    blood_request = get_object_or_404(BLoodRequest, pk=pk)
    if request.method == 'POST':
        blood_request.is_donate = True
        blood_request.save()
        return redirect('blood_requests_list')
    
def complete_blood_donation_details(request, pk):
    blood_request = get_object_or_404(BLoodRequest, pk=pk)
    if request.method == 'POST':
        blood_request.is_donate = True
        blood_request.save()
        return redirect('blood_request_details', pk=pk)
# Emergency Blood request Part
@login_required
def create_emergency_blood_request(request):
    if request.method == 'POST':
        form = EmergencyBLoodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.requester = request.user
            blood_request.save()
            return redirect('home')  
    else:
        form = EmergencyBLoodRequestForm()
    return render(request, 'donationcenters/emergency_Blood_request_form.html', {'form': form})

def emergency_blood_requests_list(request):
    emergency_blood_requests_list = EmergencyBloodRequest.objects.order_by('-created_at')
    paginator = Paginator(emergency_blood_requests_list, 5)  

    page_number = request.GET.get('page')
    try:
        blood_requests = paginator.page(page_number)
    except PageNotAnInteger:
        blood_requests = paginator.page(1)
    except EmptyPage:
        blood_requests = paginator.page(paginator.num_pages)

    return render(request, 'donationcenters/emergency_blood_request_list.html', {'blood_requests': blood_requests})


def emergency_blood_request_details(request, pk):
    blood_request = get_object_or_404(EmergencyBloodRequest, pk=pk)
    return render(request, 'donationcenters/emergengy_blood_request_details.html', {'blood_request': blood_request})

def is_admin_user(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# .............