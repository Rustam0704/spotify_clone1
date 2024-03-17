from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from apps.user.api_endpoints.Follow import UserFollowView, UserUnfollowView, ArtistFollowView, FollowersListCreateView, \
    FollowingsListCreateView, ArtistUnfollowView
from apps.user.api_endpoints.UserList import UserListView

urlpatterns = [
    path('token/', obtain_auth_token),
    path('user-follow/', UserFollowView.as_view()),
    path('user-unfollow/', UserUnfollowView.as_view()),
    path('followers/', FollowersListCreateView.as_view()),
    path('followings/', FollowingsListCreateView.as_view()),
    path('artist-follow/', ArtistFollowView.as_view()),
    path('artist-unfollow/', ArtistUnfollowView.as_view()),
    path('users/', UserListView.as_view()),

]
