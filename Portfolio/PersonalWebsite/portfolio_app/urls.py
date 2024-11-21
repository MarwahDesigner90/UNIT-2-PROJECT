from django.urls import path
from . import views

app_name ="portfolio_app"

urlpatterns = [
    path("", views.home_view , name="home_view"),
    path("experience/", views.experience_view , name="experience_view"),
    path("skills/", views.skills_view , name="skills_view"),
    path("add/experience/", views.add_experience_view , name="add_experience_view"),
    path("detail/<experience_id>/", views.detail_experience_view , name="detail_experience_view"),
    path("update/<experience_id>/",views.update_experience_view , name="update_experience_view"),
    path("delete/<experience_id>/",views.delete_experience_view , name="delete_experience_view"),
]