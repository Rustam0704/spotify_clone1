from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.music.models import Artist
from apps.user.api_endpoints.Follow.ArtistFollow.serailizers import FollowSerializer
from apps.user.api_endpoints.Follow.ArtistUnfollow.serailizers import ArtistUnFollowSerializer
from apps.user.models import User


class ArtistUnfollowView(APIView):
    authentication_classes = [TokenAuthentication, ]
    def post(self, request):
        user = request.user
        serializer = ArtistUnFollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artist_id = serializer.validated_data['artistid']
        following_artist = self.get_follow_artist(artist_id=artist_id)
        self.unfollow_to_artist(user, following_artist)
        return Response(data={'detail': 'You are successfully unfollewed'}, status=status.HTTP_202_ACCEPTED)
    def get_follow_artist(self, artist_id) -> Artist:
        user = get_object_or_404(User, id=artist_id)
        return user

    def unfollow_to_artist(self, user, following_artist):
        if following_artist in user.artist_following.all():
            user.userprofile.unfollow(following_artist)
            user.save()
        else:
            raise APIException('You are not following')


__all__ = ['ArtistUnfollowView', ]
