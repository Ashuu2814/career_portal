from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm
from .forms import ProfileUpdateForm
from .models import Profile

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse


def create_admin(request):

    if not User.objects.filter(username="admin").exists():

        User.objects.create_superuser(
            username="admin",
            email="admin@gmail.com",
            password="Admin@12345"
        )

        return HttpResponse("Admin created")

    return HttpResponse("Admin already exists")
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def user_login(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):

    logout(request)

    return redirect('home')

@login_required
def dashboard(request):

    return render(request, 'dashboard.html')


@login_required
def profile(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return redirect('profile')

    else:

        form = ProfileUpdateForm(instance=profile)

    return render(
        request,
        'profile.html',
        {'form': form}
    )