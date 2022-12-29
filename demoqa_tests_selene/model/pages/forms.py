from demoqa_tests_selene.model.controls import dropdown, modal, datepicker, checkbox, radiobutton
from demoqa_tests_selene.utils.path_files import *


def open_form_registration():
    browser.open('/automation-practice-form')


def set_name(value):
    browser.element('//input[@placeholder="First Name"]').type(value)


def set_lastname(value):
    browser.element('//input[@placeholder="Last Name"] ').type(value)


def set_mail(value):
    browser.element('//input[@placeholder="name@example.com"]').type(value)


def set_gender(gender):
    radiobutton.set_value(browser.all('[name=gender]'), gender)


def set_number(number):
    browser.element('//input[@placeholder="Mobile Number"]').type(number)


def set_date_birth(month, year, day):
    datepicker.set_date_birth(month, year, day)


def set_subjects(subjects):
    browser.element('#subjectsInput').type(subjects).press_enter()


def set_hobby(hobby):
    checkbox.checkboxes_click(browser.all('[for^=hobbies-checkbox]'), hobby)


def upload_file(file):
    download_files('#uploadPicture', file)


def set_address(address):
    browser.element('//textarea[@placeholder="Current Address"]').type(address)


def set_state(state):
    dropdown.selection_from_list('#react-select-3-input', state)


def set_city(city):
    dropdown.selection_from_list('#react-select-4-input', city)


def sending_form():
    browser.element('#submit').press_enter()


def registration_form_validation(*value):
    modal.check_form('.table-responsive td:nth-child(2)', *value)






