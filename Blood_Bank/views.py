from django.shortcuts import render
from Accounts.models import UserProfile
from django.contrib.auth.models import User


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    user_profiles_list = UserProfile.objects.select_related('user').all()
    paginator = Paginator(user_profiles_list, 3)

    page = request.GET.get('page')
    try:
        user_profiles = paginator.page(page)
    except PageNotAnInteger:
        user_profiles = paginator.page(1)
    except EmptyPage:
        user_profiles = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'user_profiles': user_profiles})

