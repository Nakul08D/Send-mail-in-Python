from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import contact_info
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def contactinfo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        mess=request.POST.get('message')
        
        st=contact_info.objects.create(name=name,number=number,email=email,message=mess)
        st.save()

        subject= "We got your problem,Our client contact Soon.."
        message= mess
        #from_email ="sagarthakur3449@gmail.com",
        recipetlist = "email"

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email],fail_silently=False)
            send_mail('Client Query','Message from : ' + name + 'Contact number:' + number + ' and email :' + email + 'there issue:' + mess , settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],fail_silently=False)
            messages.success(request, "Your mail has been send.")
        except Exception as e:
            print(e)

            

    return render(request,'contact.html')