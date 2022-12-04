from selene import browser
import os
from selene import have


def test_sending():
    browser.open('/automation-practice-form')
    browser.element('//input[@placeholder="First Name"]').type('Anna')
    browser.element('//input[@placeholder="Last Name"] ').type('Vishnyakova')
    browser.element('//input[@placeholder="name@example.com"]').type('mypochta@pochta.ru')
    browser.element('//input[@id="gender-radio-3"] ').click()
    browser.element('//input[@placeholder="Mobile Number"]').type('89000000000')

    browser.element('//input[@id="dateOfBirthInput"]').click()
    browser.element('//select[@class="react-datepicker__month-select"]').click()
    browser.element('//select[@class="react-datepicker__month-select"]/option[@value="6"]').click()
    browser.element('//select[@class="//select[@class="react-datepicker__year-select"]').click()
    browser.element('//select[@class="react-datepicker__year-select"]/option[@value="1994"]').click()
    browser.element('//div[@class="react-datepicker__day react-datepicker__day--003 react-datepicker__day--weekend"]').click()

    browser.element('#subjectsInput').type('All subjests')
    browser.element('//label[@for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').set_value(os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, 'С/Users/annavishnyakova/Downloads/test.png')))

    browser.element('//textarea[@placeholder="Current Address"]').type('Москва Кузнецкий мост')

    browser.element("//div[text()='NCR']").click().press_enter()
    browser.element("//div[text()='Delhi']").click().press_enter()

    browser.all('//div[@class="col-12 mt-4 col-md-6"]').should(have.texts(
        'Anna',
        'Vishnyakova',
        'mypochta@pochta.ru',
        '89000000000',
        '03 July,1994',
        'test.png',
        'Москва Кузнецкий мост'
        'NCR Delhi'
    ))












