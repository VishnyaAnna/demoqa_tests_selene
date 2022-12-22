from functions.use_elements import *
from functions.download_files import *


def open_form_registration():
    open_page('/automation-practice-form')


def set_name(value):
    data_entry('//input[@placeholder="First Name"]', value)


def set_lastname(value):
    data_entry('//input[@placeholder="Last Name"] ', value)


def set_mail(value):
    data_entry('//input[@placeholder="name@example.com"]', value)


def set_gender(gender):
    browser.all('[for^=gender-radio]').by(
        have.exact_text(gender)
    ).first.click()


def set_number(number):
    data_entry('//input[@placeholder="Mobile Number"]', number)


def set_date_birth(month, year, day):
    select_click('#dateOfBirthInput')
    select_click('.react-datepicker__month-select')
    select_click(f'[value="{month}"]')
    select_click('.react-datepicker__year-select')
    select_click(f'[value="{year}"]')
    select_click(f'.react-datepicker__day--00{day}')


def set_subjects(subjects):
    selection_from_list('#subjectsInput', subjects)


def set_hobby(hobby):
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()


def upload_file(file):
    download_files('#uploadPicture', file)


def set_address(address):
    data_entry('//textarea[@placeholder="Current Address"]', address)


def set_state(state):
    selection_from_list('#react-select-3-input', state)


def set_city(city):
    selection_from_list('#react-select-4-input', city)


def sending_form():
    selection_element('#submit')


def registration_form_validation(*value):
    check_form('.table-responsive td:nth-child(2)', *value)





