from django.shortcuts import render
from Accounts.models import UserProfile
from django.contrib.auth.models import User
from Accounts.constants import BLOOD_GROUP,GENDER,DISTRICT_CHOICES
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.urls import reverse




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
    paginator = Paginator(user_profiles_list, 6)
    page = request.GET.get('page')

    try:
        user_profiles = paginator.page(page)
    except PageNotAnInteger:
        user_profiles = paginator.page(1)
    except EmptyPage:
        user_profiles = paginator.page(paginator.num_pages)

    # Constructing the filter URL......
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






