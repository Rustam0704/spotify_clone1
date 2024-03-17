from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from apps.user.api_endpoints.UserList.serailizers import UserListSerializer
from apps.user.debugger import debugger
from apps.user.models import User


class UserListView(ListAPIView):
    queryset = User.objects.all().prefetch_related('followings', 'artist_following')
    serializer_class = UserListSerializer

    @method_decorator(cache_page(60 * 15))
    @debugger
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ('UserListView',)
