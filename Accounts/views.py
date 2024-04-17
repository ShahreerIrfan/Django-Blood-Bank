from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render, get_object_or_404
from .models import UserProfile, UserAddress
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from Accounts.models import UserProfile, UserAddress
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserProfileForm()
    return render(request, 'accounts/signup.html', {'form': form})




# Login part.......

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



# Logout .........

def logout_view(request):
    logout(request)
    return redirect('home')


# Profile part

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.get(user=user)
    user_address = UserAddress.objects.get(user=user)
    context = {
        'user': user,
        'profile': user_profile,
        'address': user_address
    }
    return render(request, 'accounts/profile.html', context)





