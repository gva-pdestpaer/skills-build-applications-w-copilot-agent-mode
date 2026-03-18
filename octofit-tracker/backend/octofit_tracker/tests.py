from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@hero.com', username='TestHero', password='password')
        self.team = Team.objects.create(name='TestTeam', members=[self.user.email])
        self.activity = Activity.objects.create(user_email=self.user.email, activity_type='Test', duration=10)
        self.leaderboard = Leaderboard.objects.create(team='TestTeam', points=50)
        self.workout = Workout.objects.create(name='TestWorkout', description='Test Desc')

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
