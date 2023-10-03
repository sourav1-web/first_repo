import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject2.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import *
fake = Faker()


def populate(n):
    for i in range(n):
        frollno=fake.random_int(101,999)
        fname=fake.name()
        fmarks=fake.random_int(10,100)
        femail=fake.email()
        faddr=fake.address()
        student_record=Student.objects.get_or_create(rollno=frollno,name=fname,email=femail,addr=faddr,marks=fmarks)

 
n=int(input('enter how student to add '))
populate(n)
print(f'{n} reocrd inserted')        
