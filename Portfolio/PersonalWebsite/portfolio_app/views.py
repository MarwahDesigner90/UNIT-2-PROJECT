from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
# from.models import Plant

# Create your views here.

def home_view(request:HttpRequest):
    return render(request, "portfolio_app/home.html")

def experience_view(request:HttpRequest):
    # portfolio_items = PortfolioItem.objects.all()
    # context = {
    #     'portfolio_item_1': portfolio_items[0] if len(portfolio_items) > 0 else None,
    #     'portfolio_item_2': portfolio_items[1] if len(portfolio_items) > 1 else None,
    # }
    return render(request, "portfolio_app/experience.html" ,  {})

def skills_view(request:HttpRequest):
    return render(request, "portfolio_app/skills.html")
