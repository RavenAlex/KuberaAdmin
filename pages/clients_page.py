import os
import random
import time
import keyboard

from selenium.webdriver import Keys

from locators.clients_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
from generator.generator import generated_kys_type


class PersonalAccountPage(BasePage):
    locators = PersonalAccountPageLocators()


    def auth_superadmin_int(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CLIENTS_BUTTON).click()

    def sort_kyc_type(self):
        count_before = self.element_is_visible(self.locators.COUNT).text
        self.element_is_visible(self.locators.KYC_TYPE).click()
        type_kyc = random.sample(next(generated_kys_type()).kyc_name, k=1)
        test = self.element_is_visible(self.locators.KYC_TYPE_FIELD)
        test.send_keys(type_kyc)
        test.send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.KYC_RESIDENT).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(1)
        count_after = self.element_is_visible(self.locators.COUNT).text
        return count_before, count_after

    def sort_citizenship(self):
        count_before = self.element_is_visible(self.locators.COUNT).text
        self.element_is_visible(self.locators.CITIZENSHIP_COUNTRY).click()
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(1)
        count_after = self.element_is_visible(self.locators.COUNT).text
        return count_before, count_after

    def sort_product_id(self):
        count_before = self.element_is_visible(self.locators.COUNT).text
        self.element_is_visible(self.locators.PRODUCT_ID).click()
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(1)
        count_after = self.element_is_visible(self.locators.COUNT).text
        return count_before, count_after

    def sort_date(self):
        count_before = self.element_is_visible(self.locators.COUNT).text
        self.element_is_visible(self.locators.START_DATE_BUTTON).click()
        start_input = self.element_is_visible(self.locators.START_DATE_INPUT)
        start_input.send_keys('01.04.2023')
        self.element_is_visible(self.locators.END_DATE_BUTTON).click()
        end_input = self.element_is_visible(self.locators.END_DATE_INPUT)
        end_input.send_keys('10.04.2023')
        self.element_is_visible(self.locators.CITIZENSHIP_COUNTRY).click()
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(2)
        count_after = self.element_is_visible(self.locators.COUNT).text
        return count_before, count_after

    def search_eon_id(self):
        self.element_is_visible(self.locators.SEARCH_EON_ID_BUTTON).click()
        search_eon_id = self.element_is_visible(self.locators.SEARCH_INPUT)
        search_eon_id.send_keys('EON-2CPWX-LFDWR-239ZW')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(5)
        self.element_is_visible(self.locators.EON_ID_CLIENT).click()
        time.sleep(1)
        client_uuid = self.element_is_visible(self.locators.CLIENT_UUID).text
        return client_uuid


    def kyc_orders(self):
        self.element_is_visible(self.locators.KYC_ORDERS).click()
        time.sleep(1)
        self.element_is_visible(self.locators.START_ORDER_DATE_BUTTON).click()
        start_order_input = self.element_is_visible(self.locators.START_ORDER_DATE_INPUT)
        start_order_input.send_keys('01.04.2023')
        self.element_is_visible(self.locators.END_ORDER_DATE_BUTTON).click()
        end_order_input = self.element_is_visible(self.locators.END_ORDER_DATE_INPUT)
        end_order_input.send_keys('09.04.2023')
        self.element_is_visible(self.locators.GO_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.RESULT_ORDER_BUTTON).click()
        order_id = self.element_is_visible(self.locators.ORDER_ID).text
        self.element_is_visible(self.locators.CLOSE_ORDER_BUTTON).click()
        return order_id


    def kyc_orders_report(self):
        self.element_is_visible(self.locators.KYC_ORDERS).click()
        time.sleep(1)
        self.element_is_visible(self.locators.GET_REPORT_BUTTON).click()
        self.element_is_visible(self.locators.REPORT_FROM_DATE_BUTTON).click()
        report_date_from = self.element_is_visible(self.locators.REPORT_FROM_DATE)
        report_date_from.send_keys('01.04.2023')
        self.element_is_visible(self.locators.EMPTY_PLACE).click()
        self.element_is_visible(self.locators.REPORT_TO_DATE_BUTTON).click()
        report_date_to = self.element_is_visible(self.locators.REPORT_TO_DATE)
        report_date_to.send_keys('09.04.2023')
        self.element_is_visible(self.locators.EMPTY_PLACE).click()
        self.element_is_visible(self.locators.REPORT_FINAL_BUTTON).click()
        time.sleep(2)
        result_of_report = self.element_is_visible(self.locators.RESULT_OF_REPORT).text
        path = '/Users/alexa/Downloads/Kyc_orders_report.zip'
        os.remove(path)
        return result_of_report

