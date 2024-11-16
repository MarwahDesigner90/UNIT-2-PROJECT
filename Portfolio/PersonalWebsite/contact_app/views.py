from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse

def contact_view(request:HttpRequest):

    return render(request,"contact_app/contact_form.html")

def inquiries_view(request:HttpRequest):

    return render(request, "contact_app/inquiries_messages.html")
