from selene.support.shared import browser
import os
import tests


def path(selector, file):
    browser.element(selector).set_value(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'resources/{file}'))
    )
