from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer


class ArtistUnFollowSerializer(Serializer):
    artistid = IntegerField()
