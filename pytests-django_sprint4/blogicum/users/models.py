from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    bio = models.TextField('Биография', blank=True)
