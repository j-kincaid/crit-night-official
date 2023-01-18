from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist.')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        # logs user into browser's cookies
            return redirect('profiles')
        else:
            print('Username or password is incorrect.')

    return render(request, 'panelists/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, "panelists/profiles.html", context)



    # profile = Profile.objects.get(id=pk)
    
    # # context = {"profile": profile}
    
    # return render(request, "panelists/panelist-profile.html", context)

def panelistProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request, 'panelists/panelist-profile.html', context)

