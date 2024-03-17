from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListCreateAPIView

from apps.user.api_endpoints.Follow.UserFollowersList.serailizers import UserFollowersSerializer
from apps.user.debugger import debugger
from apps.user.models import User


class FollowersListCreateView(ListCreateAPIView):
    queryset = User.objects.all().prefetch_related("followings",)
    serializer_class = UserFollowersSerializer

    # select_related O2M O20
    # prefetch_related M2M, M2O

# {
#     "user_object post commentlar",
# }

    @method_decorator(cache_page(60 * 10)) # time data
    @debugger
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ('FollowersListCreateView',)
