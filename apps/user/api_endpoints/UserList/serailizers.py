from rest_framework.serializers import ModelSerializer

from apps.music.models import Artist
from apps.user.models import User


class FollowingsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=('username',)

class MiniArtisSeriailizer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('fullname', )


class UserListSerializer(ModelSerializer):
    followings = FollowingsSerializer(many=True)
    artist_following = MiniArtisSeriailizer(many=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'artist_following', 'followings')
