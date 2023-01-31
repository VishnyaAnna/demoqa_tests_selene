import datetime

from demoqa_tests_selene.model.data.user import User, State, City, Subject, Gender, Hobbies
from demoqa_tests_selene.model.pages.practice_form import Practice_form


def test_student_registration():
    student = User(first_name='Anna',
                   last_name='Vishnyakova',
                   email='anna@gmail.com',
                   phone_number='8000000000',
                   birthday=datetime.date(1994, 7, 3),
                   subject=[Subject.Arts, Subject.Maths],
                   gender=Gender.Male,
                   hobbies=[Hobbies.Sports, Hobbies.Music],
                   picture='test.png',
                   address='Moscow',
                   state=State.Uttar_Pradesh,
                   city=City.Lucknow)
    automation_form = Practice_form()
    automation_form.open_page()
    automation_form.fill_form(student)

    automation_form.assert_registration_student(student)
