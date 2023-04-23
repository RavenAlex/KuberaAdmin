import random
import time


from selenium.webdriver import Keys

from generator.generator import generated_sort_product, generated_sort_type
from locators.auth_and_roles_locators import AuthAndRolePageLocators, TransactionSearchLocators, \
    TestSecurityManagerPageLocators
from pages.base_page import BasePage


class AuthAndRolePage(BasePage):
    locators = AuthAndRolePageLocators()

    def auth_superadmin_role_int(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys('agureev')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Clarus007')
        self.element_is_visible(self.locators.TWOFACTORAUTH).send_keys('123456')
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

    def search_transaction(self):
        self.element_is_visible(self.locators.TRANSACTION_TAB).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys('9dda5395-6ff1-48ef-bf15-f55dde2cf71d')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        time.sleep(1)
        transaction = self.element_is_present(self.locators.SEARCH_RESULT).text
        return str(transaction.split('\n')[1:-2])

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


