from django.contrib import admin
from polls.models import Registration, Addinquiry

# Register your models here.

class AdminRegistration(admin.ModelAdmin) :
    list_display = ['id', 'name', 'mail', 'pswd', 'roll', 'Date']

class AdminAddinquiry(admin.ModelAdmin) :
    list_display = ['id', 'name', 'mail', 'InquiryDate', 'status', 'call_done']

admin.site.register(Registration, AdminRegistration)    
admin.site.register(Addinquiry, AdminAddinquiry)