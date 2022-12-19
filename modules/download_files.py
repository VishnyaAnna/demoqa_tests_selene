from selene.support.shared import browser
import os


def download_files(element, file):
    browser.element(element).set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, file)))
