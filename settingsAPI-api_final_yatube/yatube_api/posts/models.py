from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        blank=True)


class Post(models.Model):
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.TextField(null=True, blank=False)
    group = models.ForeignKey(Group, null=True, blank=True,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', blank=False)
    text = models.TextField(blank=True)
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
