from datetime import date
from django.utils.timezone import now
from .models import UserWorkoutPlan
from .utils import generate_daily_workout
from users.models import Profile

class WorkoutGenerationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated:
            from datetime import date

            # Ensure you access the Profile instance
            try:
                from django.shortcuts import get_object_or_404
                profile = get_object_or_404(Profile, user=request.user)
                print(profile, request.user)
                print(profile.bmi)
                # profile = request.user.profile

                # Check if today's workout exists
                if not UserWorkoutPlan.objects.filter(user=profile, date_created=date.today()).exists():
                    workout_plan = generate_daily_workout(profile)  # Pass the profile, not the user

                    # Save the generated plan
                    for workout in workout_plan["workouts"]:
                        UserWorkoutPlan.objects.create(
                            user=request.user,
                            name=workout["name"],
                            category=workout["category"],
                            description=workout["description"],
                            duration=workout["duration"],
                            date=workout_plan["date"],
                        )
            except Profile.DoesNotExist:
                pass  # Handle the case where the profile does not exist
        return self.get_response(request)