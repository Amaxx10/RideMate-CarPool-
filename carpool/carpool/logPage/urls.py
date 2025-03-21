from django.urls import path 
# from django.conf.urls import url
from . import views

app_name = 'logPage'

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
	path('' , views.index , name = "index"),
	path('register.html' , views.register , name = "register"),
	path('forgot-password.html' , views.forget , name = "forget"),
	path('option/' , views.drive_or_ride , name = "option"),
	path('registerUser/' , views.addUser , name = "registerUser"),
	path('verifyUser/' , views.verifyUser , name = "authenticate"),
]

