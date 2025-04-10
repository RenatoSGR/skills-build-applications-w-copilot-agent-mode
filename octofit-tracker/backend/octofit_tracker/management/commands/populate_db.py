from django.core.management.base import BaseCommand
from django.utils import timezone
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import users_data, teams_data, activities_data, workouts_data
import datetime
import random

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Add test users
        self.stdout.write('Creating test users...')
        users = {}
        for user_data in users_data:
            user = User.objects.create(
                email=user_data['email'],
                name=user_data['name'],
                password=user_data['password']
            )
            users[user.email] = user
            self.stdout.write(f'Created user: {user.name}')
        
        # Add test teams
        self.stdout.write('Creating test teams...')
        teams = {}
        for team_data in teams_data:
            team = Team.objects.create(name=team_data['name'])
            
            # Assign random users to teams (2-3 users per team)
            team_members = random.sample(list(users.values()), random.randint(2, 3))
            team.members = team_members
            team.save()
            
            teams[team.name] = team
            self.stdout.write(f'Created team: {team.name} with {len(team_members)} members')
        
        # Add test activities
        self.stdout.write('Creating test activities...')
        for activity_data in activities_data:
            # Assign each activity to a random user
            random_user = random.choice(list(users.values()))
            
            activity = Activity.objects.create(
                user=random_user,
                activity_type=activity_data['activity_type'],
                duration=activity_data['duration'],
                date=activity_data['date']
            )
            self.stdout.write(f'Created activity: {activity.activity_type} for {random_user.name}')
        
        # Add test workouts
        self.stdout.write('Creating test workouts...')
        for workout_data in workouts_data:
            workout = Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description']
            )
            self.stdout.write(f'Created workout: {workout.name}')
        
        # Create leaderboard entries for each team
        self.stdout.write('Creating leaderboard entries...')
        for team in teams.values():
            points = random.randint(50, 500)
            leaderboard = Leaderboard.objects.create(
                team=team,
                points=points
            )
            self.stdout.write(f'Created leaderboard entry for {team.name}: {points} points')
        
        self.stdout.write(self.style.SUCCESS('Database successfully populated with test data!'))
