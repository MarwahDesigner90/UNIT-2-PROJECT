# # dashboard_app/forms.py
# from django import forms
# from .models import PortfolioItem 
# from .models import ContactSubmission

# class PortfolioItemForm(forms.ModelForm):
#     class Meta:
#         model = PortfolioItem
#         fields = ['title', 'description', 'image', 'link']


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactSubmission
#         fields = ['name', 'email', 'service', 'message']
#         widgets = {
#             'message': forms.Textarea(attrs={'rows': 4}),
#         }
