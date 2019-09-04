import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','forth_project.settings')

import django
django.setup()

import random
from forth_app.models import User
from faker import Faker

fakegen = Faker()
def populate(n=10):
    for entry in range(n):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()

        userrecord = User.objects.get_or_create(ufirst_name=fake_first,ulast_name=fake_last,uemail=fake_email)[0]

if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print("Polulation complete")
