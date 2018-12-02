from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def index(request):
    if request.method == 'POST':
        # Get form values
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contacts = Contact(name=name, email=email, 
        message=message)

        contacts.save()

        # send_mail(
        #     'Email received from ' + name,
        #     'You have received an email from your personal page. Check the admin panel to see message.',
        #     email,
        #     ['oscarcastro_777@hotmail.com'],
        #     fail_silently=False,
        # )

        messages.success(request, 'Your message has been sent. I will get back to you shortly!')    
    return render(request, 'contact/contact.html')

