from selene.support.shared import browser
import os
from selene import have


def test_sending():
    browser.open('/automation-practice-form')
    browser.element('//input[@placeholder="First Name"]').type('Anna')
    browser.element('//input[@placeholder="Last Name"] ').type('Vishnyakova')
    browser.element('//input[@placeholder="name@example.com"]').type('mypochta@pochta.ru')
    browser.element('//label[text()="Other"]').click()
    browser.element('//input[@placeholder="Mobile Number"]').type('89000000000')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1994"]').click()
    browser.element('.react-datepicker__day--003').click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('//label[@for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'files/test.png')))

    browser.element('//textarea[@placeholder="Current Address"]').type('Москва')

    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()

    browser.element('#submit').press_enter()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Anna Vishnyakova',
        'mypochta@pochta.ru',
        'Other',
        '8900000000',
        '03 July,1994',
        'Maths',
        'Sports',
        'test.png',
        'Москва',
        'Haryana Panipat'
    ))












