from django.urls import path 
from . import views
from rider.models import ride
app_name = 'driver'

urlpatterns = [
	path('' , views.driverHome , name = "driverHome"),
	path('driverInfo' , views.driverInfo , name = "driverInfo"),
	path('driveProcess' ,views.searchRider , name = "searchRider"),
	path('accept' ,views.acceptRider , name = "acceptRider" ),
	path('end', views.endRide , name ="endRide"),
    path('driver_dashboard', views.driver_dashboard, name='driver_dashboard'),
    path('history', views.driver_history, name='driver_history'),
    path('coupons', views.driver_coupons, name='driver_coupons'),
]

