from django import forms
from .models import UserWorkoutPlan

class UserWorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = UserWorkoutPlan
        fields = ['workout' ,'completed']