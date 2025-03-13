from django.shortcuts import render,redirect
from django.http import HttpResponse ,Http404
from django.template import loader
from django.shortcuts import render , get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import ride
import numpy as np
import googlemaps 
import json

from django.core import serializers

from django.http import JsonResponse


# Create your views here.

def index(request):
	print(request.user.username)
	return render(request , "riderHome.html" , {'username' : request.user.username})
	# return HttpResponse("<h1>SUCCESS</h1>")

def rideInfo(request):
	if request.method == "POST":
		print(request.POST['userId'])
		print(request.POST['pickup'])
		print(request.POST['destination'])
		print(request.POST['latVal'])
		print(request.POST['lngVal']) 
		print(type(request.POST))
		r = ride(
			userId = request.POST['userId'], 
			pickUp = request.POST['pickup'],
			destination = request.POST['destination']
		)
		r.save()
		context ={'paramDict' : {'userId' : request.POST['userId'],'pickup' : request.POST['pickup'] , 'latVal' : request.POST['latVal'] , 
					'lngVal' : request.POST['lngVal'] , 'destination' : request.POST['destination'] }}
		#model of ride created
	return render(request , "blank.html" , context)

def statusUpdate(request):
	print("here ----------------------------------")
	id = request.GET['id']
	update =request.GET['update']
	gmaps = googlemaps.Client(key='AIzaSyDkjrKQpyT2ps1ZrKpe8aJmb2wWbr5GlsQ') 
	rideDetils = get_object_or_404(ride, pk=id)
	my_dist_1 = gmaps.distance_matrix(rideDetils.pickUp , rideDetils.destination)['rows'][0]['elements'][0]["distance"]["value"]
	my_dist_1 = my_dist_1/1000.0
	my_dist_1 = int(my_dist_1 *10)
	print("hello ----------------------------------",id)
	if rideDetils.status :
		if rideDetils.complete:
			return JsonResponse({'success':True,'driverId':rideDetils.driverId,'complete':True,'cost':my_dist_1, 'expectedTime':rideDetils.expectedTime})
		else:
			return JsonResponse({'success':True,'driverId':rideDetils.driverId,'complete':False,'cost':my_dist_1, 'expectedTime':rideDetils.expectedTime})
	return JsonResponse({'success':False,'driverId':"none",'complete':False,'cost':0, 'expectedTime':rideDetils.expectedTime})

## UNCOMMENT - if we redirect to new page after ride acceptance
def rideSuccessful(request):
	print("kkk ----------------------------------")
	if request.method == "POST":
		id = request.POST['userId']
		print("rider id", id)
		rideDetails = get_object_or_404(ride, pk=id)
	#return render(request, 'polls/results.html', {'rideDetails': rideDetails})
	return HttpResponse("<h1>SUCCESS </h1>")

def ride_confirmation(request):
	return render(request, "ride_confirmation.html")

def search_rides(request):
    if request.method == "GET":
        return render(request, "search_rides.html")
    elif request.method == "POST":
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        
        available_rides = ride.objects.filter(
            status=False,
            pickUp__icontains=origin,
            destination__icontains=destination
        )
        
        return render(request, "search_rides.html", {
            'rides': available_rides,
            'search_performed': True
        })

def offer_ride(request):
    if request.method == "GET":
        return render(request, "offer_ride.html")
    elif request.method == "POST":
        new_ride = ride(
            userId=request.user.username,
            pickUp=request.POST['pickup'],
            destination=request.POST['destination'],
            expectedTime=request.POST.get('expected_time', '30'),
            status=False,
            complete=False
        )
        new_ride.save()
        return render(request, "ride_confirmation.html", {'ride': new_ride})

def my_rides(request):
    user_rides = ride.objects.filter(userId=request.user.username)
    return render(request, "my_rides.html", {
        'rides': user_rides,
        'username': request.user.username
    })

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('logPage:index')

    try:
        total_rides = ride.objects.filter(userId=request.user.username).count()
        completed_rides = ride.objects.filter(userId=request.user.username, complete=True).count()
        
        context = {
            'total_rides': total_rides,
            'points': completed_rides * 10,
            'username': request.user.username
        }
        return render(request, 'riderDashboard.html', context)
    except Exception as e:
        print(f"Dashboard error: {e}")
        return redirect('rider:ride')

def coupons(request):
    if not request.user.is_authenticated:
        return redirect('logPage:index')
        
    sample_coupons = [
        {'code': 'RIDE10', 'description': '10% off your next ride', 'valid_until': '2024-12-31'},
        {'code': 'FIRST50', 'description': '50% off your first ride', 'valid_until': '2024-12-31'},
    ]
    return render(request, 'riderCoupons.html', {
        'coupons': sample_coupons,
        'username': request.user.username
    })

def ride_history(request):
    if not request.user.is_authenticated:
        return redirect('logPage:index')
        
    # rides_history = ride.objects.filter(userId=request.user.username).order_by('-id')
    formatted_rides = [{
            'date': '05/02/2025',
            'pickup': 'Bhopal Railway Station, Bajariya, Navbahar Colony, Bhopal, Madhya Pradesh, India',
            'destination': 'New Delhi, Delhi, India',
            'amount': 1000,
            'status': 'Completed'
        },{
            'date': '02/01/2025',
            'pickup': 'CSMT, Mumbai, Maharashtra, India',
            'destination': 'Andheri, Mumbai, Maharashtra, India',
            'amount': 457,
            'status': 'Pending'
        }]
    
    # for r in rides_history:
    #     formatted_rides.append({
    #         'date': r.id,
    #         'pickup': r.pickUp,
    #         'destination': r.destination, 
    #         'amount': r.cost,
    #         'status': 'Completed' if r.complete else 'Ongoing' if r.status else 'Pending'
    #     })
    
    return render(request, 'riderHistory.html', {
        'rides': formatted_rides,
        'username': request.user.username
    })