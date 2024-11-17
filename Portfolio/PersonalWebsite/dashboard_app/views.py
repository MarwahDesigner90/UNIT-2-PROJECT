from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from portfolio_app.models import PortfolioItem
from contact_app.models import ContactSubmission
from .forms import PortfolioItemForm, ContactForm

# Create your views here.

def dashboard_control_view(request:HttpRequest):
    query = request.GET.get('q')
    order = request.GET.get('order', 'created_at')  # Default order
    
    experiences = PortfolioItem.objects.all()
    inquiries = ContactSubmission.objects.all()

    if query:
        experiences = experiences.filter(title__icontains=query)
        inquiries = inquiries.filter(name__icontains=query)
    
    experiences = experiences.order_by('created_at')
    inquiries = inquiries.order_by('submitted_at')

    return render(request, "dashboard_app/dashboard_control.html" , {"inquiries":inquiries, "experiences":experiences})

# def create_item_view(request):
#     if request.method == 'POST':
#         form = PortfolioItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = PortfolioItemForm()

#     return render(request, 'dashboard_app/item_form.html', {'form': form})

# def update_item_view(request, pk):
#     item = get_object_or_404(PortfolioItem, pk=pk)
#     if request.method == 'POST':
#         form = PortfolioItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = PortfolioItemForm(instance=item)

#     return render(request, 'dashboard_app/item_form.html', {'form': form})

# def delete_item_view(request, pk):
#     item = get_object_or_404(PortfolioItem, pk=pk)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('dashboard')

#     return render(request, 'dashboard_app/item_confirm_delete.html', {'item': item})