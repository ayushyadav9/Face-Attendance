from django.urls import path
from . import views 
urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.loginuser,name='base'),
    path('register',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path("attendeeList",views.Attendee_list,name='AttendeeList')
]