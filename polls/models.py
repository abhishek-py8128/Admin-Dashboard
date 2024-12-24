from django.db import models

# Create your models here.

STATUS_CHOICE = (
    ('Admin', 'Admin'),
    ('User', 'User')
)

class Registration(models.Model) :
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    pswd = models.CharField(max_length=100)
    roll = models.CharField(max_length=50, default='User',choices=STATUS_CHOICE)
    Date = models.DateTimeField(auto_now_add=True)
    
    def register(self) :
        self.save()
    
    def isExists(self) :
        if Registration.objects.filter(mail = self.mail) :
            return True
        else :
            return False

class Addinquiry(models.Model) :
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    InquiryDate = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50)
    call_done = models.BooleanField(default=False)
    
    def get_all_Inquiry_Data() :
        return  Addinquiry.objects.all()
    
    def __str__(self):
        return f"{self.name} - {self.InquiryDate}"
