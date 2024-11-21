from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpRequest , HttpResponse
from portfolio_app.models import PortfolioItem 

def home_view(request:HttpRequest):
    return render(request, "portfolio_app/home.html")

def experience_view(request:HttpRequest):
    experiences = PortfolioItem.objects.all()

    return render(request, "portfolio_app/experience.html" , {"experiences":experiences})

def skills_view(request:HttpRequest):
    return render(request, "portfolio_app/skills.html")

def add_experience_view(request:HttpRequest):
    if request.method == "POST":
        experiences= PortfolioItem( title=request.POST["title"] , description=request.POST["description"],image=request.FILES["image"], background_color=request.POST["background_color"])
        experiences.save()
        return redirect('portfolio_app:experience_view')  # Redirect to the experienc



    return render(request, "portfolio_app/add_experience.html")

def detail_experience_view(request:HttpRequest , experience_id:int):
    experiences =PortfolioItem.objects.get(pk=experience_id)
    return render(request, "portfolio_app/experience_detail.html", {"experiences" : experiences})




def update_experience_view(request: HttpRequest, experience_id: int):
    experience = get_object_or_404(PortfolioItem, pk=experience_id)

    if request.method == 'POST':
        experience.title = request.POST.get('title', experience.title)
        experience.description = request.POST.get('description', experience.description)
        experience.background_color = request.POST.get('background_color', experience.background_color)

        # Check if an image was uploaded
        if 'image' in request.FILES:
            experience.image = request.FILES['image']

        experience.save()
        return redirect('dashboard_app:dashboard_control_view')  # Change this to your desired redirect view

    return render(request, "portfolio_app/update_experience.html", {"experiences": experience})

def delete_experience_view(request:HttpRequest , experience_id:int):

 experiences =PortfolioItem.objects.get(pk=experience_id)
 experiences.delete()

 return redirect('contact_app:dashboard_control_view')




