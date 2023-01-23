from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm


def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            print(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print("Username OR password is incorrect")

    return render(request, "panelists/login_register.html")


def logoutUser(request):
    logout(request)
    messages.error(request, "You have been logged out.")
    return redirect("login")


def registerUser(request):
    page = "register"
    context = {}
    return render(request, "panelists/login_register.html", context)


#     form =CustomUserCreationForm()

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
# # Makes sure the username is lowercase

#             messages.success(request, 'User Account was created.')

#             login(request, user)
#             return redirect('profiles')

#         else:
#             messages.success(
#                 request, 'An error has occurred during registration.')

#     context = {'page': page, 'form': form}
#     return render(request, 'panelists/login_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "panelists/profiles.html", context)

    # profile = Profile.objects.get(id=pk)

    # # context = {"profile": profile}

    # return render(request, "panelists/panelist-profile.html", context)


def panelistProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profiles": profiles}

    # topSkills = profile.skill_set.exclude(description__exact="")
    # otherSkills = profile.skill_set.filter(description="")

    context = {"profile": profile}
    return render(request, "panelists/panelist-profile.html", context)


@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile

    context = {"profile": profile}
    return render(request, "panelists/account.html", context)
