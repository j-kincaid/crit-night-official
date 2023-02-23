from rest_framework import serializers
from artworks.models import Artwork, Tag, Review
from panelists.models import Profile

"""
The Serializer will import the Artwork, Tag and Profile models as JSON objects.

"""



class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Review
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag
        fields = '__all__'

class ArtworkSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta: 
        model = Artwork
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data