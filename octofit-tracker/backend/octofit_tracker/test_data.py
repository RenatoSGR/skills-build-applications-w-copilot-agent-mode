"""
Test data for OctoFit Tracker application
This file contains sample data structures matching our models
to be used for populating the database
"""

# Users data
users_data = [
    {"email": "john.smith@school.edu", "name": "John Smith", "password": "password123"},
    {"email": "sarah.jones@school.edu", "name": "Sarah Jones", "password": "password123"},
    {"email": "mike.brown@school.edu", "name": "Mike Brown", "password": "password123"},
    {"email": "lisa.white@school.edu", "name": "Lisa White", "password": "password123"},
    {"email": "alex.green@school.edu", "name": "Alex Green", "password": "password123"},
    {"email": "teacher.coach@school.edu", "name": "Coach Johnson", "password": "securepass"}
]

# Teams data - will be populated with user references in the command
teams_data = [
    {"name": "Track Stars"},
    {"name": "Swimming Champions"},
    {"name": "Basketball Elite"}
]

# Activities data - will be populated with user references in the command
activities_data = [
    {"activity_type": "Running", "duration": 30, "date": "2025-04-01"},
    {"activity_type": "Swimming", "duration": 45, "date": "2025-04-01"},
    {"activity_type": "Basketball", "duration": 60, "date": "2025-04-02"},
    {"activity_type": "Weight Training", "duration": 40, "date": "2025-04-03"},
    {"activity_type": "Yoga", "duration": 30, "date": "2025-04-03"},
    {"activity_type": "Cycling", "duration": 50, "date": "2025-04-04"}
]

# Workouts data
workouts_data = [
    {
        "name": "Morning Cardio",
        "description": "Start your day with a 30-minute cardio workout to boost energy levels."
    },
    {
        "name": "Strength Training",
        "description": "Focus on building muscle strength with weights and resistance training."
    },
    {
        "name": "Swimming Drills",
        "description": "Improve your swimming technique with these specialized drills."
    },
    {
        "name": "Basketball Skills",
        "description": "Work on dribbling, shooting, and defensive skills for basketball."
    },
    {
        "name": "Flexibility and Recovery",
        "description": "Stretch and recover with yoga poses and relaxation techniques."
    }
]
