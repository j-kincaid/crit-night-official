from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Artwork
from .forms import ArtworkForm


# This is the path  http://127.0.0.1:8000/artworks/
def artworks(request):
    artworks = Artwork.objects.all()
    context = {"artworks": artworks}
    return render(request, "artworks/artworks.html", context)


# http://127.0.0.1:8000/artwork/1/
def artwork(request, pk):
    artworkObj = Artwork.objects.get(id=pk)
    tags = artworkObj.tags.all()
    print("artworkObj:", artworkObj)
    return render(
        request, "artworks/single-artwork.html", {"artwork": artworkObj, "tags": tags}
    )


@login_required(login_url="login")
def createArtwork(request):
    form = ArtworkForm()
    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("artworks")

    context = {"form": form}
    return render(request, "artworks/artwork_form.html", context)


@login_required(login_url="login")
def updateArtwork(request, pk):
    artwork = Artwork.objects.get(id=pk)
    form = ArtworkForm(instance=artwork)

    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect("artworks")

    context = {"form": form}
    return render(request, "artworks/artwork_form.html", context)


@login_required(login_url="login")
def deleteArtwork(request, pk):
    artwork = Artwork.objects.get(id=pk)
    if request.method == "POST":
        artwork.delete()
        return redirect("artworks")
    context = {"object": artwork}
    return render(request, "artworks/delete_template.html", context)
