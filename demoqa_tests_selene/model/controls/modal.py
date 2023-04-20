from selene.support.shared import browser
from selene import have


def check_form(form, *value):  # проверка заполнения формы
    browser.all(form).should(have.texts(*value))
