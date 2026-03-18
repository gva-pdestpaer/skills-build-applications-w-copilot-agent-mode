from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        marvel_heroes = [
            {'email': 'ironman@marvel.com', 'username': 'IronMan'},
            {'email': 'captain@marvel.com', 'username': 'CaptainAmerica'},
            {'email': 'thor@marvel.com', 'username': 'Thor'},
        ]
        dc_heroes = [
            {'email': 'batman@dc.com', 'username': 'Batman'},
            {'email': 'superman@dc.com', 'username': 'Superman'},
            {'email': 'wonderwoman@dc.com', 'username': 'WonderWoman'},
        ]
        for hero in marvel_heroes + dc_heroes:
            User.objects.create_user(email=hero['email'], username=hero['username'], password='password')

        # Create teams
        Team.objects.create(name='Marvel', members=[h['email'] for h in marvel_heroes])
        Team.objects.create(name='DC', members=[h['email'] for h in dc_heroes])

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', activity_type='Running', duration=30)
        Activity.objects.create(user_email='batman@dc.com', activity_type='Cycling', duration=45)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Squats', description='Do 30 squats')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
