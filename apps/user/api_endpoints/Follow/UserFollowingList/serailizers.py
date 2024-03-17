from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer, ModelSerializer

from apps.music.models import Artist
from apps.user.models import User


class FollowingSerailizer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('fullname', )


class UserFollowingsSerializer(ModelSerializer):
    artist_following = FollowingSerailizer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'artist_following',)

