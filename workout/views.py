from django.shortcuts import render,redirect,get_object_or_404
import random
from datetime import date
from .models import Workout, WorkoutGroup,UserWorkoutPlan
from django.http import JsonResponse 
from .forms import UserWorkoutPlanForm
from django.contrib.auth.decorators import login_required




def mark_workout_completed(request, workout_id):
    if request.user.is_authenticated:
        try:
             daily_workout = UserWorkoutPlan.objects.get(id=workout_id, user=request.user)
             daily_workout.completed = True
             daily_workout.save()
             return JsonResponse({"success": True, "message": "Workout marked as completed."})
        except UserWorkoutPlan.DoesNotExist:
             return JsonResponse({"success": False, "message": "Workout not found."})
    return JsonResponse({"success": False, "message": "User not authenticated."})


def edit_workout_plan(request, workout_id):
    # Get the workout plan for the current user
    workout_plan = get_object_or_404(UserWorkoutPlan, id=workout_id, user=request.user)

    if request.method == 'POST':
        form = UserWorkoutPlanForm(request.POST, instance=workout_plan)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile or dashboard after saving
    else:
        form = UserWorkoutPlanForm(instance=workout_plan)

    return render(request, 'edit_workout_plan.html', {'form': form})


# Create your views here.
