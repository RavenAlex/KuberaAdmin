import random
import time

import allure
import keyboard

from selenium.webdriver import Keys
from selenium.common import TimeoutException

from generator.generator import generated_sort_product, generated_sort_type
from locators.auth_and_roles_locators import AuthAndRolePageLocators, TransactionSearchLocators, \
    TestSecurityManagerPageLocators, TestActivePaymentsPageLocators, TestRefundPaymentsPageLocators
from pages.base_page import BasePage


class AuthAndRolePage(BasePage):
    locators = AuthAndRolePageLocators()

    @allure.step('Auth superadmin role int')
    def auth_superadmin_role_int(self):
        with allure.step('filling fields'):
            self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
            self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
            self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        with allure.step('click login button'):
            self.element_is_visible(self.locators.LOGIN_BUTTON).click()
            time.sleep(1)
        superadmin_menu = self.element_is_present(self.locators.KADM_MENU).text
        return str(superadmin_menu).replace('\n', '')


class TransactionSearchPage(BasePage):
    locators = TransactionSearchLocators()

    def auth_superadmin_int(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)

    @allure.step('Search transaction')
    def search_transaction(self):
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys('9dda5395-6ff1-48ef-bf15-f55dde2cf71d')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(1)
        transaction = self.element_is_present(self.locators.SEARCH_RESULT).text
        return str(transaction.split('\n')[1:-2])

    @allure.step('Result attachment')
    def results_attachment(self):
        self.element_is_visible(self.locators.SEARCH_RESULT).click()
        data = []
        payment_id = self.element_is_present(self.locators.PAYMENT_ID).text
        recipient = self.element_is_visible(self.locators.RECIPIENT).text
        transport = self.element_is_visible(self.locators.TRANSPORT_ID).text
        amount = self.element_is_visible(self.locators.AMOUNT).text
        data1 = [payment_id, recipient, transport, amount]
        return str(data1)


class TestSecurityManagerPage(BasePage):
    locators = TestSecurityManagerPageLocators()

    def auth_superadmin_int(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)

    @allure.step('Sort security managment product')
    def sort_security_manager_product(self):
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        count_before = self.element_is_visible(self.locators.TOTAL_COUNT).text
        sort_product_id = self.element_is_visible(self.locators.PRODUCT_SORT)
        sort_product_id.click()
        sort_one = random.sample(next(generated_sort_product()).product_name, k=1)
        sort_one_input = self.element_is_visible(self.locators.PRODUCT_SORT_FIELD)
        sort_one_input.send_keys(sort_one)
        sort_one_input.send_keys(Keys.ENTER)
        time.sleep(1)
        count_after = self.element_is_visible(self.locators.TOTAL_COUNT).text
        return count_before, count_after

    @allure.step('Sort security managment type')
    def sort_security_manager_type(self):
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        count_before = self.element_is_visible(self.locators.TOTAL_COUNT).text
        sort_type = self.element_is_visible(self.locators.TYPE_SORT)
        sort_type.click()
        type_one = random.sample(next(generated_sort_type()).type_name, k=1)
        sort_one_input = self.element_is_visible(self.locators.TYPE_SORT_FIELD)
        sort_one_input.send_keys(type_one)
        sort_one_input.send_keys(Keys.ENTER)
        time.sleep(1)
        count_after = self.element_is_visible(self.locators.TOTAL_COUNT).text
        return count_before, count_after

    @allure.step('Reject security manager')
    def reject_security_manager(self):
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        date_before = self.element_is_visible(self.locators.DATE_PICKER_IN_LIST).text
        self.element_is_visible(self.locators.SECURITY_TRANSACTION).click()
        time.sleep(2)
        reject_reason = self.element_is_visible(self.locators.REJECT_REASON)
        self.go_to_element(reject_reason)
        reject_reason.send_keys('test')
        reject = self.element_is_visible(self.locators.REJECT_BUTTON)
        reject.click()
        time.sleep(2)
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        date_after = self.element_is_visible(self.locators.DATE_PICKER_IN_LIST).text
        return date_before, date_after

    @allure.step('Approve security manager')
    def approve_security_manager(self):
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        date_before = self.element_is_visible(self.locators.DATE_PICKER_IN_LIST).text
        self.element_is_visible(self.locators.SECURITY_TRANSACTION).click()
        time.sleep(2)
        approve_button = self.element_is_visible(self.locators.APPROVE_BUTTON)
        self.go_to_element(approve_button)
        approve_button.click()
        time.sleep(2)
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        date_after = self.element_is_visible(self.locators.DATE_PICKER_IN_LIST).text
        return date_before, date_after

    @allure.step('Single approve security manager')
    def single_approve_security_manager(self):
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        date_before = self.element_is_visible(self.locators.DATE_PICKER_IN_LIST).text
        self.element_is_visible(self.locators.SECURITY_TRANSACTION).click()
        time.sleep(2)
        single_approve_button = self.element_is_visible(self.locators.SINGLE_APPROVE_BUTTON)
        self.go_to_element(single_approve_button)
        single_approve_button.click()
        time.sleep(2)
        self.element_is_visible(self.locators.SECURITY_MANAGER).click()
        date_after = self.element_is_visible(self.locators.DATE_PICKER_IN_LIST).text
        return date_before, date_after

class TestActivePaymentsPage(BasePage):
    locators = TestActivePaymentsPageLocators()

    def auth_superadmin_int(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.ACTIVE_PAYMENTS).click()

    @allure.step('Sort active payments')
    def sort_active_payments(self):
        count_before = self.element_is_visible(self.locators.ACTIVE_COUNT).text
        self.element_is_present(self.locators.ACTIVE_PAYMENTS_SORT).click()
        select_before = random.randint(1, 3)
        while select_before != 0:
            keyboard.send('DOWN')
            select_before -= 1
        keyboard.send('ENTER')
        count_after = self.element_is_visible(self.locators.ACTIVE_COUNT).text
        return count_before, count_after


class TestRefundPaymentsPage(BasePage):
    locators = TestRefundPaymentsPageLocators()


    def auth_superadmin_int(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.REFUND_PAYMENTS).click()

    @allure.step('Test refund button')
    def test_refund_button(self):
        time_before = self.element_is_visible(self.locators.REFUND_TIME).text
        amount_before = self.element_is_visible(self.locators.REFUND_AMOUNT_EUR).text
        self.element_is_visible(self.locators.REFUND_BUTTON).click()
        time_after = self.element_is_visible(self.locators.REFUND_TIME).text
        amount_after = self.element_is_visible(self.locators.REFUND_AMOUNT_EUR).text
        return time_before, amount_before, time_after, amount_after




