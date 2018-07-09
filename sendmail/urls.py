from django.urls import path
from . import views

urlpatterns=[
	path('send', views.composemail, name='composemail'),
	path('', views.home, name='home')
]