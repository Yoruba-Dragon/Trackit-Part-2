import random
from datetime import date
from .models import Workout




def generate_daily_workout(user):
   
    # Fetch user profile
    profile = user

    # Determine workout intensity based on user's BMI or goals
    if profile.bmi < 18.5:
        intensity = "low"
    elif 18.5 <= profile.bmi< 25:
        intensity = "medium"
    else:
        intensity = "high"

    # Fetch workouts matching intensity
    matching_workouts = Workout.objects.filter(intensity=intensity)

    # Shuffle and select a random subset of workouts
    selected_workouts = random.sample(list(matching_workouts), min(3, len(matching_workouts)))

    # Create a daily plan
    daily_plan = {
        "date": date.today(),
        "workouts": [
            {
                "name": workout.name,
                "category": workout.category.name,
                "description": workout.description,
                "duration": workout.duration,
            }
            for workout in selected_workouts
        ],
    }
    return daily_plan
