from django.contrib import admin
from .models import UserProfile
from .models import Attendance

# Register your models here.
admin.site.register(UserProfile)

class Datetime(admin.ModelAdmin):
    list_display=('username','a_time')

admin.site.register(Attendance,Datetime)