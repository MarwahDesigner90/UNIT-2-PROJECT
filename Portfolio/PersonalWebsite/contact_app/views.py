from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from contact_app.models import ContactSubmission

def contact_view(request:HttpRequest):
      if request.method == "POST":
          inquiries = ContactSubmission( name=request.POST["name"] , email=request.POST["email"], service=request.POST["service"],message=request.POST["message"] )
          inquiries.save()

          return redirect('contact_app:inquiries_view')
      return render(request,"contact_app/contact_form.html")

   

def inquiries_view(request:HttpRequest):
    inquiries =ContactSubmission.objects.all()
    return render(request, "contact_app/inquiries_messages.html" , {"inquiries" :inquiries })


def edit_messages_view(request: HttpRequest, inquiry_id: int):
    inquiries = ContactSubmission.objects.get(pk=inquiry_id)
    
    if request.method == 'POST':
        inquiries.name = request.POST['name']
        inquiries.email = request.POST['email']
        inquiries.message = request.POST['message']
        inquiries.service = request.POST['service']
        inquiries.save()
        
        
        return redirect('dashboard_app:dashboard_control_view')

    return render(request, "contact_app/edit_messages.html", {"inquiries": inquiries})

def delete_messages_view(request: HttpRequest, inquiry_id: int):

 inquiries =ContactSubmission.objects.get(pk=inquiry_id)
 inquiries.delete()

 return redirect('dashboard_app:dashboard_control_view')
