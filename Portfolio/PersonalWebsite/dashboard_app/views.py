from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse

# Create your views here.

def dashboard_control_view(request:HttpRequest):
    return render(request, "dashboard_app/dashboard_control.html")