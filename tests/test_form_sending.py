from demoqa_tests_selene.model.data.student import *
from demoqa_tests_selene.model.pages.forms import *


def test_sending():
    a_vishnyakova = Student(
        first_name='Anna',
        last_name='Vishnyakova',
        email='mypochta@pochta.ru',
        phone='89000000000',
        address='Москва',
        birthday=date(1994, 7, 3),
        gender=Gender.Female,
        subject=[Subject.Maths],
        hobby=[Hobby.Sports],
        image='test.png',
        state=State.Haryana,
        city=City.Panipat)

    open_form_registration()
    fill_form(a_vishnyakova)
    # set_name('Anna')
    # set_lastname('Vishnyakova')
    # set_mail('mypochta@pochta.ru')
    # set_gender('Female')
    # set_number('89000000000')
    # set_date_birth('6', '1994', '3')
    # set_subjects('Maths')
    # set_hobby('Sports')
    # upload_file('files/test.png')
    # set_address('Москва')
    # set_state('Haryana')
    # set_city('Panipat')
    sending_form()

    registration_form_validation('Anna Vishnyakova',
                                 'mypochta@pochta.ru',
                                 'Female',
                                 '8900000000',
                                 '03 July,1994',
                                 'Maths',
                                 'Sports',
                                 'test.png',
                                 'Москва',
                                 'Haryana Panipat')
