import datetime
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Literal, List


class Hobby(Enum):
    Music = 'Music',
    Reading = 'Reading',
    Sports = 'Sports'


class Gender(Enum):
    Male = 'Male',
    Female = 'Female',
    Other = 'Other'


class Subject(Enum):
    Maths = 'Maths',
    Accounting = 'Accounting',
    Arts = 'Arts',
    SocialStudies = 'Social Studies',
    English = 'English',
    Chemistry = 'Chemistry',
    Physics = 'Physics',
    ComputerScience = 'Computer Science',
    Economics = 'Economics',
    History = 'History',
    Civics = 'Civics',
    Commerce = 'Commerce',
    Biology = 'Biology',
    Hindi = 'Hindi'


class State(Enum):
    NCR = 'NCR',
    UttarPradesh = 'Uttar Pradesh',
    Haryana = 'Haryana',
    Rajasthan = 'Rajasthan'


class City(Enum):
    Karnal = 'Karnal',
    Panipat = 'Panipat',
    Delhi = 'Delhi',
    Gurgaon = 'Gurgaon',
    Noida = 'Noida',
    Agra = 'Agra',
    Merrut = 'Merrut',
    Lucknow = 'Lucknow',
    Jaipur = 'Jaipur',
    Jaiselmer = 'Jaiselmer'


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    hobby: List[Hobby]
    image: str
    gender: Gender
    subjects: List[Subject]
    state: State
    city: City


# a_vishnyakova = Student(
#     first_name='Anna',
#     last_name='Vishnyakova',
#     email='mypochta@pochta.ru',
#     phone='89000000000',
#     address='Москва',
#     birthday=date(1994, 7, 3),
#     gender= Gender.Female,
#     subject=[Subject.Maths],
#     hobby=[Hobby.Sports],
#     image='test.png',
#     state=State.Haryana,
#     city=City.Panipat)
