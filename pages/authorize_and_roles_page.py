import time

from locators.auth_and_roles_locators import AuthAndRolePageLocators
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