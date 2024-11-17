from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from portfolio_app.models import PortfolioItem 

def home_view(request:HttpRequest):
    return render(request, "portfolio_app/home.html")

def experience_view(request:HttpRequest):
    experiences = PortfolioItem.objects.all()

    return render(request, "portfolio_app/experience.html" , {"experiences":experiences})

def skills_view(request:HttpRequest):
    return render(request, "portfolio_app/skills.html")

def add_experience_view(request:HttpRequest):
    if request.method == "POST":
        experiences= PortfolioItem( title=request.POST["title"] , description=request.POST["description"],image=request.FILES["image"], background_color=request.POST["background_color"])
        experiences.save()
        return redirect('portfolio_app:experience_view')  # Redirect to the experienc



    return render(request, "portfolio_app/add_experience.html")

