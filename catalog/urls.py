"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('', menu, name='product_menu'),
    path('computers/', ShowComputers.as_view(), name='computers_list'),
    path('phones/', ShowPhones.as_view(), name='phones_list'),
    path('computers/create/', CreateComputer.as_view(), name='create_computer'),
    path('phones/create/', CreatePhone.as_view(), name='create_phone'),
    path('computers/<str:slug>/', ShowComputer.as_view(), name='computer_detail'),
    path('phones/<str:slug>/', ShowPhone.as_view(), name='phone_detail'),
    path('computers/<str:slug>/update/', UpdateComputer.as_view(), name='update_computer'),
    path('phones/<str:slug>/update/', UpdatePhone.as_view(), name='update_phone'),
    path('computers/<str:slug>/delete/', DeleteComputer.as_view(), name='delete_computer'),
    path('phones/<str:slug>/delete/', DeletePhone.as_view(), name='delete_phone'),
]
