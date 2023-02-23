from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtworkSerializer
from artworks.models import Artwork


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/artworks'},
        {'GET':'/api/artworks/id'},
        {'POST':'/api/artworks/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getArtworks(request):
    artworks = Artwork.objects.all()
    serializer = ArtworkSerializer(artworks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getArtwork(request, pk):
    artwork = Artwork.objects.get(id=pk)
    serializer = ArtworkSerializer(artwork, many=False)
    return Response(serializer.data)
