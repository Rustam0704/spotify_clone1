from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer, ModelSerializer

from apps.user.models import User


class FollowerSerailizer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class UserFollowersSerializer(ModelSerializer):
    followings = FollowerSerailizer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'followings',)

