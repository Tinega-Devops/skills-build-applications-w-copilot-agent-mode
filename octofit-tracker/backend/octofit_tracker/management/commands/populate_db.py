
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.core.models import Team, Activity, Leaderboard, Workout
User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
        ]
        for u in users:
            user = User.objects.create_user(username=u['username'], email=u['email'], password='password')
            # Optionally, add team info to user profile if extended

        # Create activities
        Activity.objects.create(user='ironman', type='run', duration=30, team='Marvel')
        Activity.objects.create(user='spiderman', type='cycle', duration=45, team='Marvel')
        Activity.objects.create(user='batman', type='swim', duration=25, team='DC')
        Activity.objects.create(user='superman', type='run', duration=60, team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=85)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
