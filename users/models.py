from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from datetime import date
from django.db.models.signals import post_save
class Goal(models.Model):# goals model
         
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    cover_image=models.ImageField(upload_to='static/images', blank=True, null=True)
   

    def __str__(self):
        return self.title



class Profile(models.Model):# profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth= models.DateField(null=True, blank=True)
    gender= models.CharField(max_length=10, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    goals = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to='uploads/profiles/', blank=True, null=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def __str__(self):
        return f"Profile of {self.user.email}"

    @property
    def bmi(self):# bmi calculator
        if self.weight and self.height:
            height_in_meters = self.height / 100
            return round(self.weight / (height_in_meters ** 2), 2)
        return 0.0
    @property
    def age(self):# age calculator
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None


