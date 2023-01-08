import datetime
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Literal, List


class Hobby(Enum):
    Music = 1,
    Reading = 2,
    Sports = 3


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: Literal['Male', 'Female', 'Other']
    subject: Literal['Maths', 'Accounting', 'Arts', 'Social Studies', 'English', 'Chemistry', 'Physics',
                     'Computer Science', 'Economics', 'History', 'Civics', 'Commerce', 'Biology', 'Hindi']
    hobby: List[Hobby]
    image: str
    state: Literal['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city: Literal['Karnal', 'Panipat', 'Delhi', 'Gurgaon', 'Noida', 'Agra', 'Merrut', 'Lucknow', 'Jaipur', 'Jaiselmer']


a_vishnyakova = Student(
    first_name='Anna',
    last_name='Vishnyakova',
    email='mypochta@pochta.ru',
    phone='89000000000',
    address='Москва',
    birthday=date(1994, 7, 3),
    gender='Female',
    subject='Maths',
    hobby=[Hobby.Sports],
    image='test.png',
    state='Haryana',
    city='Panipat')