import os
import random
import time

import allure
import keyboard

from selenium.webdriver import Keys

from locators.currencies_locators import CurrenciesPageLocators
from pages.base_page import BasePage
from generator.generator import generated_kys_type


class CurrenciesPage(BasePage):
    locators = CurrenciesPageLocators()
    def currencies_button(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CURRENCIES_BUTTON).click()

    def currency_management_search(self):
        self.element_is_visible(self.locators.CURRENCIES_SEARCH).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH_FIELD).send_keys('BTC')
        search_result = self.element_is_visible(self.locators.CURRENCIES_SEARCH_RESULT).text
        return search_result
