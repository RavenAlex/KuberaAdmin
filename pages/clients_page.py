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