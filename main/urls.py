from django.urls import path
from django.conf import settings

from . import views

secret = settings.SECRET

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('timeline', views.tokenomics, name="timeline"),
	path('login/', views.auth_login, name="login"),
	path('register/', views.register, name="register"),
	# path('register/<str:payload>', views.register, name="register"),
	path('game', views.game, name="game"),
	path('give/', views.give, name="give"),
	path('logout', views.logout_view, name="logout_view"),
	path('dashboard', views.dashboard, name="dashboard"),
	path('admins', views.admins, name="admins"),
	path('telegram/', views.telegram, name="telegram"),
	# path('telegram/'+ secret, views.telegram, name="telegram"),
]
