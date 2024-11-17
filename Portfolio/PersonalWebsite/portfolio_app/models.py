# models.py
from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/' , default="images/defult.jpg")
    background_color = models.CharField(max_length=7, default="#ffffff")  # Hex color code
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title