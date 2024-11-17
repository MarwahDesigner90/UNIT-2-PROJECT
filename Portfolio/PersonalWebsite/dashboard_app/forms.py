# # dashboard_app/forms.py
# from django import forms
from django import forms
from portfolio_app.models import PortfolioItem 
from contact_app.models import ContactSubmission

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields ="__all__"



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields ="__all__"
