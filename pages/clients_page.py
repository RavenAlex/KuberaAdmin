import os
import random
import time

import allure
import keyboard

from selenium.webdriver import Keys

from locators.clients_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
from generator.generator import generated_kys_type


class PersonalAccountPage(BasePage):
    locators = PersonalAccountPageLocators()

    @allure.step('Auth superadmin role int')
    def auth_superadmin_int(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CLIENTS_BUTTON).click()

    @allure.step('Sort KYC type')
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

    @allure.step('Sort citizenship')
    def sort_citizenship(self):
        count_before = self.element_is_visible(self.locators.COUNT).text
        self.element_is_visible(self.locators.CITIZENSHIP_COUNTRY).click()
        keyboard.send('DOWN')
        keyboard.send('ENTER')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(1)
        count_after = self.element_is_visible(self.locators.COUNT).text
        return count_before, count_after

    @allure.step('Sort product id')
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

    @allure.step('Sort date')
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

    @allure.step('Search EON-ID')
    def search_eon_id(self):
        self.element_is_visible(self.locators.SEARCH_EON_ID_BUTTON).click()
        search_eon_id = self.element_is_visible(self.locators.SEARCH_INPUT)
        search_eon_id.send_keys('EON-2CPWX-LFDWR-239ZW')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(6)
        self.element_is_visible(self.locators.EON_ID_CLIENT).click()
        time.sleep(1)
        client_uuid = self.element_is_visible(self.locators.CLIENT_UUID).text
        return client_uuid

    @allure.step('KYC orders')
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

    @allure.step('KYC orders report')
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

    @allure.step('Organization main')
    def organisation_main(self):
        self.element_is_visible(self.locators.ORGANIZATION).click()
        time.sleep(1)
        self.element_is_visible(self.locators.ORGANIZATION_SEARCH).click()
        search_input = self.element_is_visible(self.locators.ORGANIZATION_SEARCH_INPUT)
        search_input.send_keys('Roga i kopita')
        self.element_is_visible(self.locators.ORGANIZATION_SEARCH_BUTTON).click()
        time.sleep(2)
        search_result = self.element_is_visible(self.locators.ORGANIZATION_SEARCH_RESULT).text
        self.element_is_visible(self.locators.ORGANIZATION_SEARCH_CLICK).click()
        time.sleep(2)
        result_uuid = self.element_is_visible(self.locators.ORGANIZATION_SEARCH_UUID).get_attribute('value')
        return search_result, result_uuid

    @allure.step('Sort list of details')
    def list_of_details_sort(self):
        self.element_is_visible(self.locators.LIST_OF_DETAILS).click()
        time.sleep(1)
        self.element_is_visible(self.locators.ACCOUNT_ID).click()
        ac_id_field = self.element_is_visible(self.locators.ACCOUNT_ID_FIELD)
        ac_id_field.send_keys('EON-PBZER-9YGNB-P46MM')
        self.element_is_visible(self.locators.APPLY_BUTTON).click()
        time.sleep(1)
        result_table = self.element_is_visible(self.locators.TRANSPORT_ID_RESULT_TABLE).text
        self.element_is_visible(self.locators.DETAILS_BUTTON).click()
        result_details = self.element_is_visible(self.locators.TRANSPORT_ID_RESULT_DETAILS).text
        return result_table, result_details

    @allure.step('Sort list of questionnaire')
    def list_of_questionnaire(self):
        self.element_is_visible(self.locators.LIST_OF_QUESTIONNAIRES).click()
        time.sleep(1)
        order_id_before = self.element_is_visible(self.locators.ORDER_ID_OF_QUESTIONNAIRES).text
        self.element_is_visible(self.locators.INFO_BUTTON).click()
        reject_reasone = self.element_is_present(self.locators.REASON_AREA)
        self.go_to_element(reject_reasone)
        reject_reasone.send_keys('test')
        self.element_is_visible(self.locators.APPROVE_BUTTON).click()
        time.sleep(1)
        close_button = self.element_is_visible(self.locators.CLOSE_QUESTIONNAIRE_BUTTON)
        self.go_to_element(close_button)
        close_button.click()
        self.element_is_visible(self.locators.LIST_OF_QUESTIONNAIRES).click()
        order_id_after = self.element_is_visible(self.locators.ORDER_ID_OF_QUESTIONNAIRES).text
        return order_id_before, order_id_after


