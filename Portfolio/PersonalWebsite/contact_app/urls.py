from django.urls import path
from . import views

app_name = "contact_app"

urlpatterns = [
    path("contact/", views.contact_view, name="contact_view"),
    path("inquiries/", views.inquiries_view, name="inquiries_view"),
    path("edit/<inquiry_id>",views.edit_messages_view , name="edit_messages_view"),
    path("delete/<inquiry_id>",views.delete_messages_view , name="delete_messages_view"),
]