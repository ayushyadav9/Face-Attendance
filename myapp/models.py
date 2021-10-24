from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
def my_default():
    return {'foo': 'bar'}
class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name = "user_profile", on_delete=models.CASCADE, primary_key=True, null = False)
    face_data = models.JSONField(default = my_default)
    
    class Meta:
        
        ordering = ["user"]

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    username = models.CharField(max_length=122,primary_key=True,)
    a_time = models.DateTimeField()
 
    def __str__(self):
        return self.username 