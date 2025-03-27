from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def signup(request):
    print("I am in signup")
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return HttpResponse("Password and Confirm Password should be the same")

        # Check if the user already exists
        if User.objects.filter(username=email).exists():
            return HttpResponse("User already exists")

        # Create the user only if it does not exist
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        return HttpResponse("User created successfully")

    return render(request, 'authentication/signup.html')



def handlelogin(request):

    return render(request,'authentication/login.html')

def handlelogout(request):

    return render(request,'/auth/logout.html')