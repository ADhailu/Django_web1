"""
URL configuration for django_web1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1.views import home, services, register, login, about, contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_url'),
    path('register/', register, name='regist_url'),
    path('services/', services, name='services_url'),
    path('login/', login, name='login_url'),
    path('about/', about, name="about_url"),
    path('contact/', contact, name='contact_url')
]



