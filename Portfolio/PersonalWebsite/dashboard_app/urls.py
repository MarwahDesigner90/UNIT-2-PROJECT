from django.urls import path
from . import views

app_name ="dashboard_app"

urlpatterns = [
    path("dashboard/", views.dashboard_control_view , name="dashboard_control_view"),

]