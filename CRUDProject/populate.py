import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUDProject.settings')
import django
django.setup()

from demoapp.models import *
from faker import Faker
fobj = Faker()
def populate(n):
    for i in range(n):
        feno = fobj.random_int(min=101,max=999)
        fename = fobj.name()
        fesal = fobj.random_int(min=10000,max=50000)
        feaddress = fobj.city()
        emp_records = Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddress=feaddress)
populate(50)
