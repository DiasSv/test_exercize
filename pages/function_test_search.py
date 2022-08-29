import time
from random import choice
from string import ascii_lowercase
import pytest

from .base_page import BasePage
from .locators import YandexSearchLocators


class FunctionTestCaseSearch(BasePage):

    def should_be_yandex_page(self):
        self.should_be_yandex_url()
        self.should_be_yandex_search_form()

    def should_be_yandex_url(self):
        assert "yandex.ru" in self.browser.current_url, "URL LOGIN IS NOT FOUNDED"  # наличие строки "yandex.ru" в url
        # страницы

    def should_be_yandex_search_form(self):
        assert self.is_element_present(*YandexSearchLocators.SEARCH_FORM), "Search form not founded"  # наличие формы
        # поиска

    def search_only_spaces_without_error(self):
        only_spaces = '     ' # Здесь наверное можно было использовать глобальную переменную
        self.browser.find_element(*YandexSearchLocators.SEARCH_FORM).send_keys(only_spaces)
        self.browser.find_element(*YandexSearchLocators.BUTTON_SEARCH).click()
        self.is_element_present(*YandexSearchLocators.MISSPELL_MESSAGE), "Misspell message not founded"

    def search_max_lenght_misspell_message(self):
        lenght = 247
        string_val = "".join(choice(ascii_lowercase) for i in range(lenght))
        self.browser.find_element(*YandexSearchLocators.SEARCH_FORM).send_keys(string_val)
        self.browser.find_element(*YandexSearchLocators.BUTTON_SEARCH).click()
        self.is_element_present(*YandexSearchLocators.MISSPELL_MESSAGE), "Misspell message not founded"

