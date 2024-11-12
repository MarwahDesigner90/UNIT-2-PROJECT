from django.urls import path
from . import views

app_name ="portfolio_app"

urlpatterns = [
    path("", views.home_view , name="home_view"),
    path("experience/", views.experience_view , name="experience_view"),
    path("skills/", views.skills_view , name="skills_view"),
    
]