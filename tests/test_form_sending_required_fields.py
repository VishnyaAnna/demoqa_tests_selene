import allure

from demoqa_tests_selene.model.data.student import *
from demoqa_tests_selene.model.pages import practice_form
from allure_commons._allure import attach
from demoqa_tests_selene.utils import attach
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.title("demoqa форма регистрации")
def test_sending():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver

    a_vishnyakova = Student(
        first_name='Anna',
        last_name='Vishnyakova',
        email='my@pochta.ru',
        phone='89000000000',
        address='Москва',
        birthday=date(1994, 6, 3),
        gender=Gender.Female,
        subjects=[Subject.Maths, Subject.Arts],
        hobby=[Hobby.Sports, Hobby.Music],
        image='test.png',
        state=State.Haryana,
        city=City.Panipat
    )

    with allure.step('Открываем форму регистрации'):
        practice_form.open()

    with allure.step('Заполняем только обязательные поля'):
        practice_form.required_fields_data(a_vishnyakova)

    with allure.step('Отправляем форму'):
        practice_form.submit()

    with allure.step('Проверяем форму'):
        practice_form.validation_data('Anna Vishnyakova',
                                      '',
                                      'Female',
                                      '8900000000',
                                      '03 July,1994',
                                      '',
                                      '',
                                      '',
                                      '',
                                      ''
                                      )

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
