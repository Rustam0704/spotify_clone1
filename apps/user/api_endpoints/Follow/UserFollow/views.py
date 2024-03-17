from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.music.models import Artist
from apps.user.api_endpoints.Follow.UserFollow.serailizers import FollowSerializer
from apps.user.models import User


class ArtistFollowView(APIView):
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        user = request.user
        serializer = FollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artist_id = serializer.validated_data['artistid']
        following_artist = self.get_follow_artist(artist_id=artist_id)
        self.follow_to_artist(user, following_artist)
        return Response(data={'detail': 'Successfully followed'}, status=status.HTTP_202_ACCEPTED)

    def get_follow_artist(self, artist_id) -> User:
        artist = get_object_or_404(Artist, id=artist_id)
        return artist

    def follow_to_artist(self, user, following_artist):
        if following_artist in user.artist_following.all():
            raise APIException('You are already following')
        else:
            user.userprofile.follow(following_artist)
            user.save()


__all__ = ['ArtistFollowView', ]
