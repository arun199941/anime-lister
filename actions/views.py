#Actions vieews.py
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['second_name']
        username  = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username = username).exists():
            messages.error(request,'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email is already taken')
            return redirect('register')
        else:
            user= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            return redirect('login')



    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            redirect('login')
    return render(request,'login.html')

