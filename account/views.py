from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
               messages.info(request, "Email Taken")
               return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, last_name=last_name, first_name=first_name)
                user.save()
                messages.info(request, "User Created")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['Password']
         
         user = auth.authenticate(username=username, password=password)
       
         if user is not None:
             auth.login(request, user)
             print("Heyyyyyy")
             return redirect('travel/index')
         else:
             messages.info(request, "invalid Credentials")
             return redirect('login')

    else:
         return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')