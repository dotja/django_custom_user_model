from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('create_new_user/', views.create_new_user, name='create_new_user'),
]

