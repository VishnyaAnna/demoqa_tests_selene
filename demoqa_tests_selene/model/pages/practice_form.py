from demoqa_tests_selene.model.controls import dropdown, modal, datepicker, checkbox, radiobutton
from demoqa_tests_selene.model.data.student import Student
from demoqa_tests_selene.utils.path_files import *


def open():
    browser.open('/automation-practice-form')


def set_name(value):
    browser.element('//input[@placeholder="First Name"]').type(value)


def set_lastname(value):
    browser.element('//input[@placeholder="Last Name"] ').type(value)


def set_mail(value):
    browser.element('//input[@placeholder="name@example.com"]').type(value)


def set_gender(gender):
    radiobutton.set_value(browser.all('[name=gender]'), gender.value[0])


def set_number(number):
    browser.element('//input[@placeholder="Mobile Number"]').type(number)


def set_date_birth(birthday):
    datepicker.set_date_birth(day=birthday.day, month=birthday.month, year=birthday.year)


def set_subjects(subjects):
    for r in subjects:
        browser.element('#subjectsInput').type(r.value[0]).press_enter()


def set_hobby(hobby):
    for r in hobby:
        checkbox.checkboxes_click(browser.all('[for^=hobbies-checkbox]'), r.value[0])


def upload_file(file):
    path('#uploadPicture', file)


def set_address(address):
    browser.element('//textarea[@placeholder="Current Address"]').type(address)


def set_state(state):
    dropdown.selection_from_list('#react-select-3-input', state)


def set_city(city):
    dropdown.selection_from_list('#react-select-4-input', city.value[0])


def submit():
    browser.element('#submit').press_enter()


def validation_data(*value):
    modal.check_form('.table-responsive td:nth-child(2)', *value)


def fill_data(student: Student):
    set_name(student.first_name)
    set_lastname(student.last_name)
    set_mail(student.email)
    set_gender(student.gender)
    set_number(student.phone)
    set_date_birth(student.birthday)
    set_subjects(student.subjects)
    set_hobby(student.hobby)
    upload_file(student.image)
    set_address(student.address)
    set_state(student.state)
    set_city(student.city)
