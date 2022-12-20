from functions.download_files import *
from functions.forms import *
from functions.elements import *


def test_sending():
    open_page('/automation-practice-form')
    data_entry('//input[@placeholder="First Name"]', 'Anna')
    data_entry('//input[@placeholder="Last Name"] ', 'Vishnyakova')
    data_entry('//input[@placeholder="name@example.com"]', 'mypochta@pochta.ru')
    select_click('//label[text()="Other"]')
    data_entry('//input[@placeholder="Mobile Number"]', '89000000000')

    select_click('#dateOfBirthInput')
    select_click('.react-datepicker__month-select')
    select_click('[value="6"]')
    select_click('.react-datepicker__year-select')
    select_click('[value="1994"]')
    select_click('.react-datepicker__day--003')

    selection_from_list('#subjectsInput', 'Maths')
    select_click('//label[@for="hobbies-checkbox-1"]')

    download_files('#uploadPicture', 'files/test.png')

    data_entry('//textarea[@placeholder="Current Address"]', 'Москва')

    selection_from_list('#react-select-3-input', 'Haryana')
    selection_from_list('#react-select-4-input', 'Panipat')

    selection_element('#submit')

    check_form('.table-responsive td:nth-child(2)',
               'Anna Vishnyakova',
               'mypochta@pochta.ru',
               'Other',
               '8900000000',
               '03 July,1994',
               'Maths',
               'Sports',
               'test.png',
               'Москва',
               'Haryana Panipat')
