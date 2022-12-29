from selene.support.shared import browser


def selection_from_list(element, value):
    browser.element(element).type(value).press_enter()
