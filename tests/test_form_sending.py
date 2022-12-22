from functions.forms import *


def test_sending():
    open_form_registration()
    set_name('Anna')
    set_lastname('Vishnyakova')
    set_mail('mypochta@pochta.ru')
    set_gender('Female')
    set_number('89000000000')
    set_date_birth('6', '1994', '3')
    set_subjects('Maths')
    set_hobby('Sports')
    upload_file('files/test.png')
    set_address('Москва')
    set_state('Haryana')
    set_city('Panipat')
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
