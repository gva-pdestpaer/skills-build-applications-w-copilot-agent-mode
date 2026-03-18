from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_users_permissions',
        blank=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
