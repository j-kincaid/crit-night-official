from rest_framework import serializers
from artworks.models import Artwork 

"""
The Serializer will import the Artwork model as a JSON object

"""


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Artwork
        fields = '__all__'