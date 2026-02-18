from django.core.management.base import BaseCommand
from tracker.models import Team, User, Workout, Activity, LeaderboardEntry

class Command(BaseCommand):
    help = "Populate octofit_db with test data for OctoFit Tracker."

    def handle(self, *args, **options):
        team_a, _ = Team.objects.get_or_create(name="Team A")
        team_b, _ = Team.objects.get_or_create(name="Team B")

        u1, _ = User.objects.get_or_create(username="mona", defaults={"team": team_a})
        u2, _ = User.objects.get_or_create(username="octocat", defaults={"team": team_b})

        w1, _ = Workout.objects.get_or_create(name="Run", defaults={"calories_burned": 300})
        w2, _ = Workout.objects.get_or_create(name="Yoga", defaults={"calories_burned": 150})

        Activity.objects.get_or_create(user=u1, workout=w1, defaults={"duration_minutes": 30})
        Activity.objects.get_or_create(user=u2, workout=w2, defaults={"duration_minutes": 45})

        LeaderboardEntry.objects.get_or_create(user=u1, defaults={"points": 100})
        LeaderboardEntry.objects.get_or_create(user=u2, defaults={"points": 80})

        self.stdout.write(self.style.SUCCESS("Test data populated successfully."))
