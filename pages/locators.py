from selenium.webdriver.common.by import By


class YandexSearchLocators():
    SEARCH_FORM = (By.CSS_SELECTOR, "input.input__control")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button.button_theme_search")
    MISSPELL_MESSAGE = (By.CSS_SELECTOR, "div.misspell__message")
