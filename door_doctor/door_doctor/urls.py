"""door_doctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('about_us/', views.AboutUs.as_view(), name='about'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('services/', views.Services.as_view(), name='services'),
    path('faq/', views.FAQ.as_view(), name='faq'),
    path('contact/', views.contact.as_view(), name='contact')
]
