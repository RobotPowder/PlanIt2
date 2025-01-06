from django.urls import path
from . import views

app_name = 'LoginSesion'

urlpatterns = [
	path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
]
