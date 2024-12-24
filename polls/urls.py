"""
URL configuration for AdminDashBoard project.

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
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index_View),
    path('Registration/', views.Registration_View, name='registration'),
    path('logins/', views.login, name='registration'),
    path('logout/', views.logout, name='registration'),
    path('Admin-Panel/', views.AdminPanel, name='index'),
    path('AddInquiry/',views.AddInquiry, name='Addinquiry'),
    path('InquiryGET/', views.InquiryGET, name='Addinquiry'),
    path('View-Inquiry/', views.View_inquiry, name='view_inquiry'),
    path('mark-call-done/<int:inquiry_id>/', views.View_inquiry, name='mark_call_done'),
    path('admin/', admin.site.urls),
]