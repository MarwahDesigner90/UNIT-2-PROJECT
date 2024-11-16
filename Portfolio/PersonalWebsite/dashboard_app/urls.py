from django.urls import path
from . import views

app_name ="dashboard_app"

urlpatterns = [
    path("dashboard/", views.dashboard_control_view , name="dashboard_control_view"),
    # path('create/', views.create_item_view, name='create_item_view'),
    # path('update/<int:pk>/', views.update_item_view, name='update_item_view'),
    # path('delete/<int:pk>/', views.delete_item_view, name='delete_item_view'),
]