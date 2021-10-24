from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from myapp.models import UserProfile,Attendance
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
import os
import pickle
import time
import base64
import io
from PIL import Image
import json
from django.urls import path, include
import face_recognition
import numpy as np 


def loginuser(request):
        
        if request.method=="POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
        
                # print(username)
                user = authenticate(username=username,password=password)
                if user is not None:
                        raw_face = user.user_profile.face_data
                        raw_face = np.array(json.loads(raw_face))

                        face_input = request.POST.get('encodings')
                        encodings = json.dumps(get_face_encoding_from_base64(face_input))
                        raw_encod = np.array(json.loads(encodings))
                        match = face_recognition.compare_faces([raw_face],raw_encod)       
                        if True in match:
                                #changed  
                                if Attendance.objects.filter(username = username).exists(): 
                                        Attendance.objects.filter(username=username).update(a_time=datetime.now())     
                                else:
                                        Attendance.objects.create(username = username, a_time = datetime.now())
                                login(request,user)
                                messages.success(request,"Attendance marked successfuly")
                                return redirect('profile')
                        else:
                                messages.error(request, "Face is not recognized!!")
                                return redirect('home')
                else:
                        messages.error(request, "Invalid Credentials!!")
                        return redirect('home') 
                
        return render(request,'login.html') 

      
def home(request):
   return render(request, 'home.html')

def register(request):
        if request.method=="POST":
                username=request.POST.get('usernameup')
                password=request.POST.get('passwordup')
                repassword=request.POST.get('repasswordup')
                if User.objects.filter(email=username).exists():
                        messages.warning(request, "User already exists, try with another username")
                        return redirect('home')
               
                if password!=repassword:
                        messages.error(request, "Password dosen't match")
                        return redirect('home')
                
                face_input = request.POST.get('encodings')
                encodings = json.dumps(get_face_encoding_from_base64(face_input))
                
                user = User.objects.create_user(username,username,password)
                user_profile = UserProfile.objects.create(user = user, face_data = encodings)
                
                return render(request,'home.html')
                
                
        return render(request,'register.html',{})
                            
def profile(request):
        return render(request,'profile.html',{})


def Attendee_list(request):
     #obj = Attendance.objects.all.()      
     obj1 = Attendance.objects.filter(a_time__date = datetime.today()).order_by('-a_time') 
     obj2 = Attendance.objects.filter(~Q(a_time__date = datetime.today())).order_by('-a_time') 
     return render(request,"A_list.html",{'obj1':obj1,'obj2':obj2 })

def get_face_encoding_from_base64(base64String):
    
    buf = io.BytesIO(base64.b64decode(base64String))
    process = face_recognition.load_image_file(buf)
    image_encoding = face_recognition.face_encodings(process)

    # print(np.shape(image_encoding[0]))

    return image_encoding[0].tolist()

        
