from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import PortfolioItem
# from .forms import PortfolioItemForm
# from .forms import ContactSubmission

# Create your views here.

def dashboard_control_view(request:HttpRequest):
    # query = request.GET.get('q')
    # order = request.GET.get('order', 'created_at')  # Default order
    
    # portfolio_items = PortfolioItem.objects.all()
    # contact_submissions = Contact.objects.all()

    # if query:
    #     portfolio_items = portfolio_items.filter(title__icontains=query)
    #     contact_submissions = contact_submissions.filter(name__icontains=query)
    
    # portfolio_items = portfolio_items.order_by(order)
    # contact_submissions = contact_submissions.order_by(order)

    return render(request, "dashboard_app/dashboard_control.html")

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