from django.db import models
from django.contrib.auth import get_user_model
import uuid


class TelegramUser(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='telegram_user'
    )
    chat_id = models.CharField(
        max_length=20
    )

    def __str__(self) -> str:
        return self.chat_id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user
        self.save()

class TgUser(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    code = models.IntegerField(unique=True)
    has_oscar = models.BooleanField(default=False)
    cover_photo = models.ImageField(upload_to='covers/', blank=True)
    year = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    actors = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre_choices = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'),
    )
    genre = models.CharField(max_length=20, choices=genre_choices)
    about = models.TextField(default='')

    def __str__(self):
        return self.title
    
class Serial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    code = models.IntegerField(unique=True)
    has_oscar = models.BooleanField(default=False)
    cover_photo = models.ImageField(upload_to='covers/', blank=True)
    year = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    actors = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre_choices = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'),
    )
    genre = models.CharField(max_length=40, choices=genre_choices, blank=True)
    about = models.TextField(default='')

    def __str__(self):
        return self.title
