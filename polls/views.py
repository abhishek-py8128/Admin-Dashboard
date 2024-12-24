from django.shortcuts import render, redirect, HttpResponse 
from polls.models import Registration, Addinquiry
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, timedelta
from django.contrib import messages
from datetime import date

# ============================ Index =================================

def index_View(request) :
    return render(request, 'registration.html')

# ============================ Signup =================================

def Registration_View(request) :

    if request.method == 'POST' :
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        pswd = request.POST.get('pswd')
        
        hashpswd = make_password(pswd)                                                      
        print('Hash Password', hashpswd)
        print(check_password(pswd, hashpswd))

        store = Registration(name=name, mail=mail, pswd=hashpswd)
    
        if store.isExists() :
            return HttpResponse('Mail Id All Ready Exists')
        store.register()
    return redirect(f'/Admin-Panel')


# ============================= Login ================================== 

def login(request) :
    if request.method == 'GET' :
        return render(request, 'registration.html')
        
    else :      
        mail = request.POST.get('mail')
       
        Customer = Registration.objects.filter(mail=request.POST['mail'])
        if Customer :
            request.session['mail'] = mail
            return redirect(f'/Admin-Panel')
        
        else :
            return HttpResponse('Mail Id Is Invalid')
        
# ============================= Logout ================================== 

def logout(request) :
    if request.session.has_key('mail') :
        del request.session['mail']
        return redirect(f'/logins')
    
    else :
        return redirect(f'/logins')         
    
        
# ============================= Admin Panel ==================================         

def AdminPanel(request) :
    if request.session.has_key('mail') :
        Data = Addinquiry.get_all_Inquiry_Data()    
        
        # Get Inquiry Dates as strings
        InquiryDate_str = [d.InquiryDate for d in Data]
        print("Inquiry Dates (strings):", InquiryDate_str)
        
        InquiryDate = []
        for date_str in InquiryDate_str:
            InquiryDate.append(datetime.strptime(date_str, "%Y-%m-%d"))
    
        # Recent Inquiries Get .
        if Data:  # Check if there are any inquiries
            most_recent_inquiry = max(Data, key=lambda i: i.InquiryDate)
            print("Most Recent Inquiry:", most_recent_inquiry)

            # If you want to store the most recent inquiry in a list
            recent_inquiries = [most_recent_inquiry]
            print(recent_inquiries)
            recentInq = len(recent_inquiries)
            print("Number of recent inquiries:", recentInq)
        else:
            print("No inquiries found.")
            
        # Get total inquiry
        TotalInquiry = len(InquiryDate)    

        # Pending Inquiries Get .
        pendingInquiry = [i for i in Data if i.status == 'pending']
        pendingInq = len(pendingInquiry)

        # Resolved Inquiries Get .
        ResolvedInquiry = [i for i in Data if i.status == 'resolved']
        resolvedInq = len(ResolvedInquiry)
        
        # Get today's date
        today_date = date.today()       
        print("Today's date:", today_date)

        # inquiries get that are today's date
        TodayInquiry = [i for i in InquiryDate if i.date() == today_date]
        todayInq = len(TodayInquiry)
        print("Today's inquiry count:", todayInq) 

        # Alert For Tomorrow
        one_days_later = [inquiry + timedelta(days=1) for inquiry in InquiryDate]
        
        # Check All Ready User Call Is Done .
        Inq = 0
        for i in Data :
            if i.call_done == False :
                TomorrowInquiry = [inquiry for inquiry in one_days_later if inquiry.date() == today_date]
                Inq = len(TomorrowInquiry)  
                print("Tomorrow's inquiry count:", Inq)        
        
        context = {
            'TotalInquiry' : TotalInquiry,
            'pendingInq' : pendingInq,
            'resolvedInq' : resolvedInq,
            'recentInq' : recentInq,
            'todayInq' : todayInq,
            'Inq' : Inq
        }       
        return render(request, 'index.html', context)        
    
    else :
        return redirect(f'/logins')         
        
# ============================= Add Inquiry ================================== 

def AddInquiry(request) :
    if request.session.has_key('mail') :
        Data = Addinquiry.get_all_Inquiry_Data()    
        
        # Get Inquiry Dates as strings
        InquiryDate_str = [d.InquiryDate for d in Data]
        print("Inquiry Dates (strings):", InquiryDate_str)
        
        InquiryDate = []
        for date_str in InquiryDate_str:
            InquiryDate.append(datetime.strptime(date_str, "%Y-%m-%d"))
    
        # Recent Inquiries Get .
        if Data:  # Check if there are any inquiries
            most_recent_inquiry = max(Data, key=lambda i: i.InquiryDate)
            print("Most Recent Inquiry:", most_recent_inquiry)

            # If you want to store the most recent inquiry in a list
            recent_inquiries = [most_recent_inquiry]
            print(recent_inquiries)
            recentInq = len(recent_inquiries)
            print("Number of recent inquiries:", recentInq)
        else:
            print("No inquiries found.")
            
        # Get total inquiry
        TotalInquiry = len(InquiryDate)    

        # Pending Inquiries Get .
        pendingInquiry = [i for i in Data if i.status == 'pending']
        pendingInq = len(pendingInquiry)

        # Resolved Inquiries Get .
        ResolvedInquiry = [i for i in Data if i.status == 'resolved']
        resolvedInq = len(ResolvedInquiry)
        
        # Get today's date
        today_date = date.today()       
        print("Today's date:", today_date)

        # inquiries get that are today's date
        TodayInquiry = [i for i in InquiryDate if i.date() == today_date]
        todayInq = len(TodayInquiry)
        print("Today's inquiry count:", todayInq) 

        # Alert For Tomorrow
        one_days_later = [inquiry + timedelta(days=1) for inquiry in InquiryDate]
        
        # Check All Ready User Call Is Done .
        Inq = 0
        for i in Data :
            if i.call_done == False :
                TomorrowInquiry = [inquiry for inquiry in one_days_later if inquiry.date() == today_date]
                Inq = len(TomorrowInquiry)  
                print("Tomorrow's inquiry count:", Inq)
        
        context = {
            'TotalInquiry' : TotalInquiry,
            'pendingInq' : pendingInq,
            'resolvedInq' : resolvedInq,
            'recentInq' : recentInq,
            'todayInq' : todayInq,
            'Inq' : Inq
        }       

        return render(request, 'Add-inquiry.html', context)
    else :
        return redirect(f'/logins')         
        
# ============================= Inquiry Get ================================== 
    
def InquiryGET(request):
    if request.session.has_key('mail'):
        name = request.GET.get('name')
        mail = request.GET.get('mail')
        InquiryDate = request.GET.get('InquiryDate')
        status = request.GET.get('status')
        
        # Save the inquiry with call_done set to False
        Addinquiry(name=name, mail=mail, InquiryDate=InquiryDate, status=status, call_done=False).save()
        return redirect(f'/View-Inquiry')
    
    else:
        return redirect(f'/logins')    

# ============================= View Inquiry ================================== 
 
def View_inquiry(request, inquiry_id=None):
    if request.session.has_key('mail'):
        if inquiry_id:  # If an inquiry ID is provided, try to mark the call as done
            try:
                inquiry = Addinquiry.objects.get(id=inquiry_id)
                inquiry.call_done = True  # Mark call as done
                inquiry.save()
                messages.success(request, 'Call status updated successfully.')
            except Addinquiry.DoesNotExist:
                messages.error(request, 'Inquiry not found.')
            return redirect('/View-Inquiry')  # Redirect after processing the update
        
        else:  # If no inquiry ID, display all inquiries
            Data = Addinquiry.get_all_Inquiry_Data()    
        
            # Get Inquiry Dates as strings
            InquiryDate_str = [d.InquiryDate for d in Data]
            print("Inquiry Dates (strings):", InquiryDate_str)
        
            InquiryDate = []
            for date_str in InquiryDate_str:
                InquiryDate.append(datetime.strptime(date_str, "%Y-%m-%d"))
    
            # Recent Inquiries Get .
            if Data:  # Check if there are any inquiries
                most_recent_inquiry = max(Data, key=lambda i: i.InquiryDate)
                print("Most Recent Inquiry:", most_recent_inquiry)

                # If you want to store the most recent inquiry in a list
                recent_inquiries = [most_recent_inquiry]
                print(recent_inquiries)
                recentInq = len(recent_inquiries)
                print("Number of recent inquiries:", recentInq)
            else:
                print("No inquiries found.")
            
            # Get total inquiry
            TotalInquiry = len(InquiryDate)    

            # Pending Inquiries Get .
            pendingInquiry = [i for i in Data if i.status == 'pending']
            pendingInq = len(pendingInquiry)

            # Resolved Inquiries Get .
            ResolvedInquiry = [i for i in Data if i.status == 'resolved']
            resolvedInq = len(ResolvedInquiry)
        
            # Get today's date
            today_date = date.today()       
            print("Today's date:", today_date)

            # inquiries get that are today's date
            TodayInquiry = [i for i in InquiryDate if i.date() == today_date]
            todayInq = len(TodayInquiry)
            print("Today's inquiry count:", todayInq) 

            # Alert For Tomorrow
            one_days_later = [inquiry + timedelta(days=1) for inquiry in InquiryDate]
            
            # Check All Ready User Call Is Done .
            Inq = 0
            for i in Data :
                if i.call_done == False :
                    TomorrowInquiry = [inquiry for inquiry in one_days_later if inquiry.date() == today_date]
                    Inq = len(TomorrowInquiry)  
                    print("Tomorrow's inquiry count:", Inq)
            
            # Get Inquiry All Data
            Data = Addinquiry.get_all_Inquiry_Data()

            context = {
                'TotalInquiry' : TotalInquiry,
                'pendingInq' : pendingInq,
                'resolvedInq' : resolvedInq,
                'recentInq' : recentInq,
                'todayInq' : todayInq,
                'Inq' : Inq, 
                'Data' : Data
            }  
                         
            return render(request, 'View-inquiry.html', context)  
    else:
        return redirect(f'/logins')   