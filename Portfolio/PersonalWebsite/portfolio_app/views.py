from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse

def home_view(request:HttpRequest):
    return render(request, "portfolio_app/home.html")

def experience_view(request:HttpRequest):

    return render(request, "portfolio_app/experience.html")

def skills_view(request:HttpRequest):
    return render(request, "portfolio_app/skills.html")

def add_experience_view(request:HttpRequest):
    return render(request, "portfolio_app/add_experience.html")

