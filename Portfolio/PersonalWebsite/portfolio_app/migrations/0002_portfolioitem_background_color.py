# Generated by Django 5.1.2 on 2024-11-16 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
    ]