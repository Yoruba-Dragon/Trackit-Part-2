from django import forms
from .models import UserWorkoutPlan,Workout

class UserWorkoutPlanForm(forms.ModelForm):# workout plan form
    class Meta:
        model = UserWorkoutPlan
        fields = ['completed']

class Workout(forms.ModelForm):#workout form , allows users to add workouts 
    class Meta:
        model= Workout
        fields= '__all__'