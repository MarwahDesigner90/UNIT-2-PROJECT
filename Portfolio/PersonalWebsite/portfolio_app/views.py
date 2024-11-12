from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
# from.models import Plant

# Create your views here.

def home_view(request:HttpRequest):
    return render(request, "portfolio_app/home.html")

def experience_view(request:HttpRequest):
    return render(request, "portfolio_app/experience.html")

def skills_view(request:HttpRequest):
    return render(request, "portfolio_app/skills.html")
