from django.shortcuts import render,redirect,get_object_or_404
import random
from datetime import date
from .models import Workout, WorkoutGroup,UserWorkoutPlan
from django.http import JsonResponse 
from .forms import UserWorkoutPlanForm
from django.contrib.auth.decorators import login_required
from users.models import Profile
from datetime import date
from django.shortcuts import redirect,get_object_or_404



def mark_workout_completed(request, workout_id):
    if request.user.is_authenticated:
        try:
             profile = get_object_or_404(Profile, user=request.user)
             daily_workout = UserWorkoutPlan.objects.get(id=workout_id, user=profile)
             daily_workout.completed = True
             daily_workout.save()
             #return JsonResponse({"success": True, "message": "Workout marked as completed."})
             return redirect('plans')
        except UserWorkoutPlan.DoesNotExist:
             return JsonResponse({"success": False, "message": "Workout not found."})
    return JsonResponse({"success": False, "message": "User not authenticated."})


def edit_workout_plan(request, workout_id):
    # Get the workout plan for the current user
    profile = get_object_or_404(Profile, user=request.user)
    workout_plan = get_object_or_404(UserWorkoutPlan, id=workout_id, user=profile)

    if request.method == 'POST':
        form = UserWorkoutPlanForm(request.POST, instance=workout_plan)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile or dashboard after saving
    else:
        form = UserWorkoutPlanForm(instance=workout_plan)

    return render(request, 'editplan.html', {'form': form})


# Create your views here.
def plans(request):
    profile = get_object_or_404(Profile, user=request.user)
    user_workout_plan=UserWorkoutPlan.objects.filter(user=profile, date_created=date.today()).first()
    workouts=Workout.objects.filter(intensity=user_workout_plan.intensity)
    context ={'profile':profile, 'user_workout_plan':user_workout_plan, 'workouts':workouts}
    return render( request, 'plans.html', context)
