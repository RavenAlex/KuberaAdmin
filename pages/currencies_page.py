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
        self.element_is_visible(self.locators.CURRENCIES_TAB).click()

    def currency_management_search(self):
        self.element_is_visible(self.locators.CURRENCIES_SEARCH).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH_FIELD).send_keys('BTC')
        search_result = self.element_is_visible(self.locators.CURRENCIES_SEARCH_RESULT).text
        return search_result

    def disable_currencies(self):
        self.element_is_visible(self.locators.CURRENCIES_SEARCH).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH_FIELD).send_keys('BTC')
        self.element_is_visible(self.locators.CURRENCY_BUTTON).click()
        disable_currency_check_box = self.element_is_present(self.locators.CURRENCY_DISABLE_CHECK_BOX)
        self.go_to_element(disable_currency_check_box)
        disable_currency_check_box.click()
        self.element_is_visible(self.locators.CURRENCY_SAVE_BUTTON).click()
        time.sleep(10)
        self.element_is_visible(self.locators.CURRENCIES_TAB).click()
        self.element_is_visible(self.locators.CURRENCY_DISABLE_SORT).click()
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        self.element_is_visible(self.locators.CURRENCIES_SEARCH).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH_FIELD).send_keys('BTC')
        self.element_is_visible(self.locators.CURRENCY_BUTTON_AFTER_DISABLE).click()
        disable_currency_check_box = self.element_is_present(self.locators.CURRENCY_DISABLE_CHECK_BOX)
        self.go_to_element(disable_currency_check_box)
        time.sleep(1)
        disable_currency_check_box.click()
        self.element_is_visible(self.locators.CURRENCY_SAVE_BUTTON).click()
        time.sleep(10)
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.CURRENCIES_TAB).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH_FIELD).send_keys('BTC')
        search_result = self.element_is_visible(self.locators.CURRENCIES_SEARCH_RESULT).text
        return search_result

    def edit_transport(self):
        self.element_is_visible(self.locators.CURRENCIES_SEARCH).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH_FIELD).send_keys('BTC')
        self.element_is_visible(self.locators.CURRENCY_BUTTON).click()
        self.element_is_visible(self.locators.CURRENCY_TRANSPORT).click()
        self.element_is_visible(self.locators.TRANSPORT_STATUS_SORT).click()
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        transport_status_before = self.element_is_visible(self.locators.TRANSPORT_STATUS).text
        self.element_is_visible(self.locators.CURRENCY_TRANSPORT_BUTTON).click()
        self.element_is_visible(self.locators.TRANSPORT_STATUS_CHANGE_CHECK_BOX).click()
        self.element_is_visible(self.locators.FEES_TAB).click()
        withdrawal_constant_fee = self.element_is_present(self.locators.WITHDRAWAL_CONSTANT_FEE)
        withdrawal_constant_fee_before = self.element_is_visible(self.locators.WITHDRAWAL_CONSTANT_FEE_FIELD).get_attribute('value')
        self.action_double_click(withdrawal_constant_fee)
        keyboard.send('DELETE')
        self.element_is_visible(self.locators.WITHDRAWAL_CONSTANT_FEE_FIELD).send_keys('0.0001')
        self.element_is_visible(self.locators.LIMIT_TAB).click()
        withdrawal_minimum_amount_before = self.element_is_visible(self.locators.WITHDRAWAL_MINIMUM_LIMIT_FIELD).get_attribute('value')
        withdrawal_minimum_amount = self.element_is_visible(self.locators.WITHDRAWAL_MINIMUM_LIMIT)
        self.action_double_click(withdrawal_minimum_amount)
        keyboard.send('DELETE')
        self.element_is_visible(self.locators.WITHDRAWAL_MINIMUM_LIMIT_FIELD).send_keys('0.1')
        self.element_is_visible(self.locators.TRANSPORT_TAB).click()
        deposit_duration_minutes_before = self.element_is_visible(self.locators.DEPOSIT_DURATION_MINUTES_FIELD).get_attribute('value')
        self.element_is_visible(self.locators.DEPOSIT_DURATION_MINUTES).click()
        keyboard.send('BACKSPACE')
        keyboard.send('BACKSPACE') #по-хорошему доделать на фронте, не работает doubleclick именно в этом поле
        self.element_is_visible(self.locators.DEPOSIT_DURATION_MINUTES_FIELD).send_keys('15')
        self.element_is_visible(self.locators.TRANSPORT_EDIT_SAVE_BUTTON).click()
        time.sleep(10)
        self.element_is_visible(self.locators.TRANSPORT_TAB_AFTER).click()
        self.element_is_visible(self.locators.TRANSPORT_STATUS_SORT).click()
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        transport_status_after = self.element_is_visible(self.locators.TRANSPORT_STATUS).text
        self.element_is_visible(self.locators.CURRENCY_TRANSPORT_BUTTON).click()
        self.element_is_visible(self.locators.TRANSPORT_STATUS_CHANGE_CHECK_BOX).click()
        self.element_is_visible(self.locators.FEES_TAB).click()
        withdrawal_constant_fee = self.element_is_present(self.locators.WITHDRAWAL_CONSTANT_FEE)
        withdrawal_constant_fee_after = self.element_is_visible(self.locators.WITHDRAWAL_CONSTANT_FEE_FIELD).get_attribute('value')
        self.action_double_click(withdrawal_constant_fee)
        keyboard.send('DELETE')
        self.element_is_visible(self.locators.WITHDRAWAL_CONSTANT_FEE_FIELD).send_keys('0.00011')
        self.element_is_visible(self.locators.LIMIT_TAB).click()
        withdrawal_minimum_amount_after = self.element_is_visible(self.locators.WITHDRAWAL_MINIMUM_LIMIT_FIELD).get_attribute('value')
        withdrawal_minimum_amount = self.element_is_visible(self.locators.WITHDRAWAL_MINIMUM_LIMIT)
        self.action_double_click(withdrawal_minimum_amount)
        keyboard.send('DELETE')
        self.element_is_visible(self.locators.WITHDRAWAL_MINIMUM_LIMIT_FIELD).send_keys('0.0003')
        self.element_is_visible(self.locators.TRANSPORT_TAB).click()
        deposit_duration_minutes_after = self.element_is_visible(
        self.locators.DEPOSIT_DURATION_MINUTES_FIELD).get_attribute('value')
        self.element_is_visible(self.locators.DEPOSIT_DURATION_MINUTES).click()
        keyboard.send('BACKSPACE')
        keyboard.send('BACKSPACE')  # по-хорошему доделать на фронте, не работает doubleclick именно в этом поле
        self.element_is_visible(self.locators.DEPOSIT_DURATION_MINUTES_FIELD).send_keys('30')
        self.element_is_visible(self.locators.TRANSPORT_EDIT_SAVE_BUTTON).click()
        return transport_status_before, transport_status_after, withdrawal_constant_fee_before, \
                withdrawal_constant_fee_after, withdrawal_minimum_amount_before, withdrawal_minimum_amount_after, \
                deposit_duration_minutes_before, deposit_duration_minutes_after

    def system_clients_search(self):
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_TAB).click()
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_SEARCH).click()
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_SEARCH_FIELD).send_keys('BEST_BARTER:int')
        search_result = self.element_is_visible(self.locators.UUID_RESULT).text
        return search_result

