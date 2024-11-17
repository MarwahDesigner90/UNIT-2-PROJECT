from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from contact_app.models import ContactSubmission

def contact_view(request:HttpRequest):
      if request.method == "POST":
          inquiries = ContactSubmission( name=request.POST["name"] , email=request.POST["email"], service=request.POST["service"],message=request.POST["message"] )
          inquiries.save()

          return redirect('contact_app:inquiries_view')
      return render(request,"contact_app/contact_form.html")

    # if request.method == "POST":
    #     inquiries = ContactSubmission(
    #         name=request.POST["name"],
    #         email=request.POST["email"].strip(),  # Remove any extra spaces
    #         service=request.POST["service"],
    #         message=request.POST["message"]
    #     )
    #     inquiries.save()
    #     return redirect('contact_app:inquiries_view')  # Redirect to inquiries view after saving

    # return render(request, "contact_app/contact_form.html" , {})  # Return the form for GET requests

def inquiries_view(request:HttpRequest):
    inquiries =ContactSubmission.objects.all()
    return render(request, "contact_app/inquiries_messages.html" , {"inquiries" :inquiries })



