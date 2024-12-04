from django.db import models
from users.models import Profile


INTENSITY=[
    ('high', 'high'),
    ('medium', 'medium'),
    ('low','low'),
]
class WorkoutGroup(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=244)
    related_goals= models.ManyToManyField(to="users.Goal")


    def __str__(self):
        return self.name


class Workout(models.Model):
    name= models.CharField(max_length=25)
    image=models.ImageField(upload_to='uploads/workouts', blank=True, null=True)
    workout_group=models.ManyToManyField(to= "WorkoutGroup")
    description = models.TextField()
    duration = models.IntegerField()
    user_workout_plan= models.ForeignKey('UserWorkoutPlan', on_delete= models.CASCADE, null=True, blank=True)
    intensity=models.CharField(default='low', max_length=20, choices=INTENSITY)
    def __str__(self):
        return self.name




class UserWorkoutPlan(models.Model):# creating the workout plans model
    
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    #workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    date_created=models.DateField(auto_now=True)
    completed= models.BooleanField(default=False)
    intensity=models.CharField(null=True, blank=True, max_length=20, default='low', choices=INTENSITY)
    def __str__(self):
        return f"{self.user} {self.date_created}"
    
