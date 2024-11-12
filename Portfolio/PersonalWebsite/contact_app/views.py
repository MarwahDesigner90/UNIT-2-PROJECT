from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def contact_view(request:HttpRequest):
    return render(request, "contact_app/contact_form.html")
