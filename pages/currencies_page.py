import os
import random
import time

import action as action
import allure
import keyboard
from keyboard import mouse

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from locators.currencies_locators import CurrenciesPageLocators
from pages.base_page import BasePage
from generator.generator import generated_kys_type


class CurrenciesPage(BasePage):
    locators = CurrenciesPageLocators()

    @allure.step('Currencies tab')
    def currencies_button(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CURRENCIES_TAB).click()

    @allure.step('Currency management search')
    def currency_management_search(self):
        self.element_is_visible(self.locators.CURRENCIES_SEARCH).click()
        self.element_is_visible(self.locators.CURRENCIES_SEARCH_FIELD).send_keys('BTC')
        search_result = self.element_is_visible(self.locators.CURRENCIES_SEARCH_RESULT).text
        return search_result

    @allure.step('Disable currencies')
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

    @allure.step('Edit transport')
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

    @allure.step('System clients search')
    def system_clients_search(self):
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_TAB).click()
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_SEARCH).click()
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_SEARCH_FIELD).send_keys('BEST_BARTER:int')
        search_result = self.element_is_visible(self.locators.UUID_RESULT).text
        return search_result

    @allure.step('indra wallets withdraw')
    def indra_wallets_withdraw(self):
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_TAB).click()
        self.element_is_visible(self.locators.INDRA_WALLETS_BUTTON).click()
        time.sleep(1)
        indra_wallet_id = self.element_is_visible(self.locators.INDRA_WALLETS_ID).text
        self.element_is_visible(self.locators.INDRA_TRX_WITHDRAW_BUTTON).click()
        indra_withdraw_name_currency = self.element_is_visible(self.locators.INDRA_WITHDRAW_CURRENCY_NAME).text
        self.element_is_visible(self.locators.INDRA_WITHDRAW_CURRENCY_AMOUNT).click()
        self.element_is_visible(self.locators.INDRA_WITHDRAW_CURRENCY_AMOUNT_FIELD).send_keys('10')
        self.element_is_visible(self.locators.INDRA_WITHDRAW_BUTTON_SUBMIT).click()
        indra_withdraw_amount_result = self.element_is_visible(self.locators.INDRA_WITHDRAW_AMOUNT_RESULT).text
        self.element_is_visible(self.locators.INDRA_WITHDRAW_CONFIRM_BUTTON).click()
        indra_withdraw_success = self.element_is_visible(self.locators.INDRA_WITHDRAW_SUCCESS).text
        return indra_wallet_id, indra_withdraw_name_currency, indra_withdraw_amount_result, indra_withdraw_success

    @allure.step('Indra saving wallets withdraw')
    def indra_saving_wallets_withdraw(self):
        self.element_is_visible(self.locators.SYSTEM_CLIENTS_TAB).click()
        self.element_is_visible(self.locators.SAVING_WALLETS_BUTTON).click()
        time.sleep(1)
        indra_saving_wallet_id = self.element_is_visible(self.locators.INDRA_SAVING_WALLETS_ID).text
        self.element_is_visible(self.locators.INDRA_SAVING_TRX_WITHDRAW_BUTTON).click()
        indra_saving_withdraw_name_currency = self.element_is_visible(self.locators.INDRA_SAVING_WITHDRAW_CURRENCY_NAME).text
        self.element_is_visible(self.locators.INDRA_SAVING_WITHDRAW_CURRENCY_AMOUNT).click()
        self.element_is_visible(self.locators.INDRA_SAVING_WITHDRAW_CURRENCY_AMOUNT_FIELD).send_keys('1')
        self.element_is_visible(self.locators.INDRA_SAVING_WITHDRAW_BUTTON_SUBMIT).click()
        indra_saving_withdraw_amount_result = self.element_is_visible(self.locators.INDRA_SAVING_WITHDRAW_AMOUNT_RESULT).text
        self.element_is_visible(self.locators.INDRA_SAVING_WITHDRAW_CONFIRM_BUTTON).click()
        indra_saving_withdraw_success = self.element_is_visible(self.locators.INDRA_SAVING_WITHDRAW_SUCCESS).text
        return indra_saving_wallet_id, indra_saving_withdraw_name_currency, indra_saving_withdraw_amount_result, \
               indra_saving_withdraw_success

    @allure.step('Clients wallets owner')
    def clients_wallets_owner(self):
        self.element_is_visible(self.locators.CLIENTS_WALLET_TAB).click()
        self.element_is_visible(self.locators.CLIENTS_WALLET_UUID).click()
        self.element_is_visible(self.locators.CLIENTS_WALLET_UUID_FIELD).send_keys('fc106c64-1f8e-40b5-bb9f-b336f1ab97f3')
        time.sleep(2)
        self.element_is_visible(self.locators.CLIENTS_WALLET_OWNER_BUTTON).click()
        clients_owner_uuid = self.element_is_visible(self.locators.CLIENTS_WALLET_OWNER_UUID).text
        print(clients_owner_uuid)

    @allure.step('Ravana servers')
    def ravana_servers(self):
        self.element_is_visible(self.locators.RAVANA_SERVERS_BUTTON).click()
        self.element_is_visible(self.locators.RAVANA_UPDATE_BUTTON).click()
        update_state_check_box = self.element_is_present(self.locators.RAVANA_UPDATE_STATE_CHECK_BOX)
        action = ActionChains(self.driver)
        action.move_to_element(update_state_check_box)
        action.click()
        action.perform()
        self.element_is_visible(self.locators.RAVANA_UPDATE_STATE_CHECK_BOX_CONFIRM).click()
        state = self.element_is_present(self.locators.RAVANA_SERVER_STATE).get_attribute('class')
        time.sleep(1)
        self.element_is_visible(self.locators.RAVANA_UPDATE_BUTTON).click()
        update_state_check_box = self.element_is_present(self.locators.RAVANA_UPDATE_STATE_CHECK_BOX)
        action = ActionChains(self.driver)
        action.move_to_element(update_state_check_box)
        action.click()
        action.perform()
        self.element_is_visible(self.locators.RAVANA_UPDATE_STATE_CHECK_BOX_CONFIRM).click()
        return state

    @allure.step('System balance update')
    def audit_system_balance_update(self):
        self.element_is_visible(self.locators.AUDIT_SYSTEM_TAB).click()
        self.element_is_visible(self.locators.AUDIT_SYSTEM_BALANCE_UPDATE).click()
        time.sleep(1)

    @allure.step('System balance ravana withdraw')
    def audit_system_balance_ravana_withdraw(self):
        self.element_is_visible(self.locators.AUDIT_SYSTEM_TAB).click()
        self.element_is_visible(self.locators.AUDIT_BALANCE_RAVANA).click()
        self.element_is_visible(self.locators.AUDIT_BALANCE_RAVANA_WITHDRAW).click()
        self.element_is_visible(self.locators.RECEIVER_RAVANA_ID_FIELD).click()
        keyboard.send('ENTER')
        self.element_is_visible(self.locators.AUDIT_BALANCE_RAVANA_WITHDRAW_AMOUNT).click()
        self.element_is_visible(self.locators.AUDIT_BALANCE_RAVANA_WITHDRAW_AMOUNT_FIELD).send_keys('0.000001')
        self.element_is_visible(self.locators.AUDIT_BALANCE_RAVANA_WITHDRAW_CONFIRM).click()
        time.sleep(1)
        audit_ravana_withdraw_result = self.element_is_visible(self.locators.AUDIT_BALANCE_RAVANA_WITHDRAW_RESULT).text
        return audit_ravana_withdraw_result

    @allure.step('Audit system allocation funds sort')
    def audit_system_allocation_funds_sort(self):
        self.element_is_visible(self.locators.AUDIT_SYSTEM_TAB).click()
        self.element_is_visible(self.locators.AUDIT_ALLOCATION_FUNDS_TAB).click()
        self.element_is_visible(self.locators.AUDIT_ALLOCATION_FUNDS_SORT).click()
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        self.element_is_visible(self.locators.AUDIT_ALLOCATION_FUNDS_UPDATE).click()
        state_one = self.element_is_visible(self.locators.AUDIT_ALLOCATION_FUNDS_STATE).text
        self.element_is_visible(self.locators.AUDIT_ALLOCATION_FUNDS_SORT).click()
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        self.element_is_visible(self.locators.AUDIT_ALLOCATION_FUNDS_UPDATE).click()
        state_two = self.element_is_visible(self.locators.AUDIT_ALLOCATION_FUNDS_STATE).text
        return state_one, state_two
