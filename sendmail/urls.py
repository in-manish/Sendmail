from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[
	path('send', views.composemail, name='composemail'),
	path('', views.home, name='home'),
	path('login', auth_views.login, name='login'),


]