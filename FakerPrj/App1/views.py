from django.shortcuts import render
from .models import PersonModel
from faker import Faker

# Create your views here.
fake_p = Faker()

def fakePersonView(request):
    persons = []

    for i in range(1):
        fake_name = fake_p.name()
        fake_address = fake_p.address()
        fake_phone_no = fake_p.phone_number()
        fake_company = fake_p.company()
        fake_email = fake_p.email()
        person = PersonModel.objects.get_or_create(name=fake_name,address=fake_address,phone_no=fake_phone_no,company=fake_company,email=fake_email)

        print(person)
        print(type(person))
        print(type(person[0]))
        print(len(person))
        persons.append(person)

    return render(request,'App1/show.html',{'persons':persons})