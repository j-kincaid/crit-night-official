from django.shortcuts import render
from .models import Profile

# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, "panelists/profiles.html", context)


def panelistProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profile": profile}
    return render(request, "panelists/panelist-profile.html", context)
