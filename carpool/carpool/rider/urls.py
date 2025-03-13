from django.urls import path 
# from django.conf.urls import url
from . import views

app_name = 'rider'

# urlpatterns = [
# 	path('' , views.index , name = "index"),
# 	url(r'^(?P<album_id>[0-9]+)/$' , views.detail , name = "detail"),
# 	url(r'^(?P<album_id>[0-9]+)/favorite/$' , views.favorite , name = "favorite")
# ]

# urlpatterns = [
# 	path('' , views.IndexView.as_view() , name = "index"),
# 	url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name = "detail"),
# 	url(r'^album/add/$', views.createAlbum.as_view() , name = "album-add")
# ]

urlpatterns = [
	path('' , views.index , name = "ride"),
	path('submit', views.rideInfo, name = "rideInfo"),
	path('processsing', views.statusUpdate, name = "statusUpdate"),
	path('success', views.rideSuccessful, name = "rideSuccessful"),
    path('ride_confirmation/', views.ride_confirmation, name = "ride_confirmation"),  # Added trailing slash
	# path('rideRemove', views.endRide, name = "endRide"),
    path('search/', views.search_rides, name='search_rides'),
    path('offer/', views.offer_ride, name='offer_ride'),
    path('my-rides/', views.my_rides, name='my_rides'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Changed from riderDashboard/
    path('coupons/', views.coupons, name='coupons'),
    path('history/', views.ride_history, name='history'),
]

