"""
URL configuration for SereneProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('index/', views.index, name='index'),
    path('package/', views.package, name='package'),
     path('narok/', views.narok, name='narok'),
     path('coast/', views.coast, name='coast'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('central/', views.central, name='central'),
path('view_order/', views.view_order, name='view_order'),
    path('login/', views.login_view, name='login'),
    path('signup/',views.signup_view, name='signup'),
    path('bookings/', views.bookings, name='bookings'),
     path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),









]
