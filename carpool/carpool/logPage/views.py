from django.shortcuts import render, redirect
from django.http import HttpResponse ,Http404
from django.template import loader
from django.shortcuts import render , get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserProfile

# Create your views here.
# from .models import user

def index(request):
	return render(request , "login.html" , {})

def drive_or_ride(request):
	print(request.user)
	return render(request  , "drive_or_ride.html" , {'user': request.user.username})

def register(request):
	print("-----------REGISTER---------------")
	context = {'userExist' : False}
	return render(request , "register.html" , context)

def forget(request):
	return render(request , "forgot-password.html" , {})

def validateForm(input):
    if User.objects.filter(username=input['userId']).exists():
        return True
    else:
        user = User.objects.create_user(
            username=input['userId'],
            email='fake@gmail.com',
            password=input['passWd']
        )
        user.first_name = input['firstName']
        user.last_name = input['lastName']
        user.save()
        
        # Create UserProfile with role
        UserProfile.objects.create(
            user=user,
            role=input['role']
        )
        return False

def addUser(request):
    if request.method == "POST":
        input = {
            'userId': request.POST['userId'],
            'passWd': request.POST['passWd'],
            'firstName': request.POST['firstName'],
            'lastName': request.POST['lastName'],
            'role': request.POST['role']
        }
        
        userExist = validateForm(input)
        if userExist:
            return render(request, "register.html", {'userExist': True})
        
        user = authenticate(username=input['userId'], password=input['passWd'])
        if user is not None:
            login(request, user)
            if input['role'] == 'driver':
                return redirect('/driver/')
            else:
                return redirect('/rider/')
    
    return render(request, "register.html", {'userExist': False})

def verifyUser(request):
    context = {'loginFail': False, 'userExist': True}
    if request.method == "POST":
        try:
            user = authenticate(request, username=request.POST["userId"], password=request.POST["passWd"])
            if user is None:
                context['loginFail'] = True
                return render(request, "login.html", context)
            else:
                login(request, user)
                # Get user role and redirect accordingly
                user_profile = UserProfile.objects.get(user=user)
                if user_profile.role == 'driver':
                    return redirect('/driver/')
                else:
                    return redirect('/rider/')
        except:
            context['userExist'] = False
            return render(request, "login.html", context)
