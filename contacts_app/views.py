from faker import Faker
from django.shortcuts import render, HttpResponse

from .models import Contact
# Create your views here.

def home(request):
    return render(template_name="home.html", request=request, context={"contacts":Contact.objects.all()})

def create(request):
    pass

def update(request):
    pass

def delete(request):
    pass

def add_contacts(request):
    for i in range(20):
        profile=Faker(locale="he_IL").simple_profile()
        phone=Faker(locale="he_IL").phone_number()
        Contact(name=profile['name'], phone=phone, email=profile['mail'], address=profile['address']).save()
    return HttpResponse("contacts created")
