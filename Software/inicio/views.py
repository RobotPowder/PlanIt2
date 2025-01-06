from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, timedelta
from django.shortcuts import render


####################################################################3 PÁGINA PRINCIPAL############################################################33
def inicio(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'inicio.html')


