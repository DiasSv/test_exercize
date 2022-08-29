import pytest

from pages.function_test_search import FunctionTestCaseSearch
from pages.base_page import BasePage

link = link = "https://yandex.ru"

def test_see_forms(browser):
    page = FunctionTestCaseSearch(browser, link)
    page.open()
    page.should_be_yandex_page()


def test_search_only_spaces(browser):
    page = FunctionTestCaseSearch(browser, link)
    page.open()
    page.search_only_spaces_without_error()

