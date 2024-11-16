from django.db import models

# Create your models here.
class ContactSubmission(models.Model):
    class Service(models.TextChoices):
        WEB_DEVELOPMENT = 'web_development', 'Web Development'
        SEO_OPTIMIZATION = 'seo_optimization', 'SEO Optimization'
        WEB_MAINTENANCE = 'web_maintenance', 'Web Maintenance'
        UI_UX_DESIGN = 'ui_ux_design', 'UI/UX Design'
        CI_CD = 'ci_cd', 'CI/CD'
        RESPONSIVE_DESIGN = 'responsive_design', 'Responsive Design'
        INQUIRIES = 'inquiries', 'Inquiries'  

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    service = models.CharField(max_length=50, choices=Service.choices)
    submitted_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"Message from {self.name} at {self.submitted_at}"