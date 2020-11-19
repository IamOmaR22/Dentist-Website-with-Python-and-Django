from django.shortcuts import render
from django.core.mail import send_mail # for mail send we need to import it
from .models import Service

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # here message-name comes from contact.html file's input type name
        message_email = request.POST['message-email']
        message = request.POST['message']

        ### Send an Email Start ###
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['omarfaruk2468@gmail.com','mehedibinhafiz@gmail.com',], # To email
        )
        ### Send an Email End ###

        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def service(request):
    service = Service.objects.all()

    return render(request, 'service.html', {'service':service})

def pricing(request):
    return render(request, 'pricing.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        ### Send an Email Start ###
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Date: " + your_date + " Message: " + your_message

        send_mail(
            'Appointment Request', # subject
            appointment, # message
            your_email, # from email
            ['omarfaruk2468@gmail.com'], # To email
            # ['omarfaruk2468@gmail.com','mehedibinhafiz@gmail.com'], # To email
        )
        ### Send an Email End ###

        return render(request, 'appointment.html', {
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_schedule':your_schedule,
            'your_date':your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})


def booknow(request):
    return render(request, 'booknow.html')
