from django.core.management.base import BaseCommand
from pymongo import MongoClient

# Populate the octofit_db database with test data

class Command(BaseCommand):
    help = "Populate octofit_db with test data (users, teams, activities, leaderboard, workouts)."

    def handle(self, *args, **options):
        # Default local Mongo (no auth) as used in the exercise
        client = MongoClient("mongodb://localhost:27017")
        db = client["octofit_db"]

        users = db["users"]
        teams = db["teams"]
        activities = db["activities"]
        workouts = db["workouts"]
        leaderboard = db["leaderboard"]

        # Optional: reset (makes re-runs deterministic)
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        workouts.delete_many({})
        leaderboard.delete_many({})

        # Teams
        team_docs = [
            {"name": "Team A"},
            {"name": "Team B"},
        ]
        teams.insert_many(team_docs)

        team_a = teams.find_one({"name": "Team A"})
        team_b = teams.find_one({"name": "Team B"})

        # Users
        user_docs = [
            {"username": "mona", "team": str(team_a["_id"])},
            {"username": "octocat", "team": str(team_b["_id"])},
        ]
        users.insert_many(user_docs)

        mona = users.find_one({"username": "mona"})
        octocat = users.find_one({"username": "octocat"})

        # Workouts
        workout_docs = [
            {"name": "Run", "calories_burned": 300},
            {"name": "Yoga", "calories_burned": 150},
        ]
        workouts.insert_many(workout_docs)

        run = workouts.find_one({"name": "Run"})
        yoga = workouts.find_one({"name": "Yoga"})

        # Activities
        activity_docs = [
            {"user": str(mona["_id"]), "workout": str(run["_id"]), "duration_minutes": 30},
            {"user": str(octocat["_id"]), "workout": str(yoga["_id"]), "duration_minutes": 45},
        ]
        activities.insert_many(activity_docs)

        # Leaderboard
        leaderboard_docs = [
            {"user": str(mona["_id"]), "points": 100},
            {"user": str(octocat["_id"]), "points": 80},
        ]
        leaderboard.insert_many(leaderboard_docs)

        self.stdout.write(self.style.SUCCESS("octofit_db populated with test data successfully."))
