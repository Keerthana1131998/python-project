from django.shortcuts import render
from . models import*
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render (request,'login.html')
def register(request):
    return render (request,'register.html')
def register_form_submission(request):
    print("*** welcome to register page***")
    first_name=request.POST.get('first_name')
    Last_name=request.POST.get('last_name')
    email_id=request.POST.get('email_id')
    phone_number=request.POST.get('phone_number')
    appointment_time=request.POST.get('appointment_time')
    reason_for_the_appointment=request.POST.get('reason_for_the_appointment')
    print(f"{first_name} {Last_name} {email_id} {phone_number} {appointment_time} {reason_for_the_appointment}")
    otp_number=random.randint(0000,9999)
    print(f"otp number is {otp_number}")
    # to save database table
    ex1=register_table(first_name=first_name,Last_name=Last_name,email_id=email_id,phone_number=phone_number,appointment_time=appointment_time,reason_for_the_appointment=reason_for_the_appointment,otp_number=otp_number)
    ex1.save()
    print(" ***registered  successfully ***")
    try:
        subject = 'Hospital Appoinment Bookings'
        message = f'Hi {first_name} {Last_name}, thank you for registering our hospital online booking.\n your otp is->{otp_number}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_id, ]
        send_mail( subject, message, email_from, recipient_list )
        print("**** mail sent successfully***")
    except:
        print("**** mail not sned .. pls check your internet or mail id***")
    return render(request,'login.html')
def login_form_submission(request):
    if register_table.objects.filter(email_id=request.POST.get('email_id'),otp_number=request.POST.get('otp_number')):
        print("login successfully")
        logger_data=register_table.objects.get(email_id=request.POST.get('email_id'),otp_number=request.POST.get('otp_number'))
        return render (request,'dashboard.html',{'logger_data':logger_data})
    else:
        print("*** Login Failed***")
        messages.error(request,'pls check email or otp number',extra_tags='failed')
        return render (request,'login.html')
def dashboard (request):
    return render (request,'dashboard.html')    


    

    