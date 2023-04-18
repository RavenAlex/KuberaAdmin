import time

from locators.auth_and_roles_locators import AuthAndRolePageLocators, TransactionSearchLocators
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
