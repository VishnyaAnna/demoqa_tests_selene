from selene.support.shared import browser
from selene import have


def open_page(url):  # открытие страниц
    browser.open(url)


def data_entry(element, value):  # ввод данных
    browser.element(element).type(value)


def selection_from_list(element, value):  # выбор из списка с вводом значения
    browser.element(element).type(value).press_enter()


def check_form(form, *value): # проверка заполнения формы
    browser.all(form).should(have.texts(*value))


def selection_element(element):  # выбор из списка
    browser.element(element).press_enter()
