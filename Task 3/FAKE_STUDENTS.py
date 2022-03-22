#!/usr/bin/env python
#pip3 install faker
from faker import Faker
import random
faker = Faker()

# generating fake name with faker package
def get_student_details():
    #for male
    male_obj={'name': faker.name_male(),
    'age': random.randint(18, 30),
    'gender': "Male",
    'address': faker.address(),
    'contact': faker.phone_number()}

    #for female
    female_obj={'name': faker.name_female(),
    'age': random.randint(18, 30),
    'gender': "Female",
    'address': faker.address(),
    'contact': faker.phone_number()}

    # randomly choice one obj 
    obj=random.choice([male_obj,female_obj])

    return obj

if __name__=="__main__":
    print(get_student_details())



