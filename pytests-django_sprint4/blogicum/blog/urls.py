from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    path('',
         views.IndexHome.as_view(),
         name='index'),
    path('posts/<int:post_id>/',
         views.PostDetailView.as_view(),
         name='post_detail'),
    path(
        'category/<slug:category_slug>/',
        views.CategoryListView.as_view(),
        name='category_posts'),
    path('posts/create/',
         views.PostCreateView.as_view(),
         name='create_post'),
    path('posts/<int:post_id>/edit/',
         views.PostUpdateView.as_view(),
         name='edit_post'),
    path('posts/<int:post_id>/delete/',
         views.PostDeleteView.as_view(),
         name='delete_post'),
    path('posts/<int:post_id>/delete_comment/<int:comment_pk>/',
         views.CommentDeleteView.as_view(),
         name='delete_comment'),
    path('posts/<int:post_id>/comment/',
         views.CommentCreateView.as_view(),
         name='add_comment'),
    path('posts/<int:post_id>/comment/<int:comment_pk>/',
         views.CommentUpdateView.as_view(),
         name='edit_comment'),
    path('profile/<str:username>/',
         views.ProfileView.as_view(),
         name='profile'),
    path('profile/<str:username>/edit/',
         views.ProfileUpdateView.as_view(),
         name='edit_profile')

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
