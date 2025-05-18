from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v1 = SimpleRouter()
router_v1.register(
    'posts', PostViewSet,
    basename='posts-processing'
)
router_v1.register(
    'groups', GroupViewSet,
    basename='groups-processing'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
    basename='comments-processing'
)
router_v1.register(
    'follow', FollowViewSet,
    basename='follow-processing'
)
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
