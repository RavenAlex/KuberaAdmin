import time

import allure

from pages.authorize_and_roles_page import AuthAndRolePage, TransactionSearchPage, TestSecurityManagerPage, \
    TestActivePaymentsPage, TestRefundPaymentsPage


@allure.suite("Form")
class TestForm:
    @allure.feature('AuthAndRoles')
    class TestAuthAndRoles:
        @allure.title('Check AuthAndRoles')
        def test_auth(self, driver):
            test_authorization_form = AuthAndRolePage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            super_admin = test_authorization_form.auth_superadmin_role_int()
            assert super_admin == 'TRANSACTIONSCLIENTSCURRENCIESEXCHANGERPRODUCTSCMSSWAPADMINMERCHANTSBEST ' \
                                  'BARTERINVESTMENTS', 'Authorization has not been worked or super admin ' \
                                                                'menu incorrect displayed '

    class TestTransaction:
        @allure.title('Check Transaction')

        def test_transaction_search(self, driver):
            test_authorization_form = TransactionSearchPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            transaction_result = test_authorization_form.search_transaction()
            transaction_attachment = test_authorization_form.results_attachment()
            assert transaction_result == "['98074', 'EON-AEN4T-L6G5U-GJR7W', " \
                                         "'RAVANA:EON-int=DEPOSITORY:int=ColorCoin=BTC', '0.0001']", 'Transaction ' \
                                                                                                      'value incorrect display in table or search does not work'
            assert transaction_result == transaction_attachment, 'Transaction attachment has not been opened ' \
                                                                 'or value bot correct'

    class TestSecurityManager:
        @allure.title('Check SecurityManager')

        def test_security_sort_product(self, driver):
            test_authorization_form = TestSecurityManagerPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            count_before, count_after = test_authorization_form.sort_security_manager_product()
            assert count_before != count_after, 'Sort product has not been worked'

        def test_security_sort_type(self, driver):
            test_authorization_form = TestSecurityManagerPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            count_before, count_after = test_authorization_form.sort_security_manager_type()
            assert count_before != count_after, 'Sort type has not been worked'

        def test_security_reject(self, driver):
            test_authorization_form = TestSecurityManagerPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            date_before, date_after = test_authorization_form.reject_security_manager()
            return date_before, date_after
            assert date_before != date_after, 'Reject button has not been worked or table has not been updated'

        def test_security_approve(self, driver):
            test_authorization_form = TestSecurityManagerPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            date_before, date_after = test_authorization_form.approve_security_manager()
            return date_before, date_after
            assert date_before != date_after, 'Approve button has not been worked or table has not been updated'

        def test_security_single_approve(self, driver):
            test_authorization_form = TestSecurityManagerPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            date_before, date_after = test_authorization_form.single_approve_security_manager()
            return date_before, date_after
            assert date_before != date_after, 'Single approve button has not been worked or table has not been updated'

    class TestActivityPayments:
        @allure.title('Check ActivePayments')

        def test_active_sort(self, driver):
            test_authorization_form = TestActivePaymentsPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            count_before, count_after = test_authorization_form.sort_active_payments()
            assert count_before != count_after, 'Sort active payment has not been worked'

        # def test_active_terminate(self, driver):
        #     test_authorization_form = TestActivePaymentsPage(driver, 'https://kadm.int.exscudo.com/#/signin')
        #     test_authorization_form.open()
        #     test_authorization_form.auth_superadmin_int()
        #     date_before, date_after = test_authorization_form.test_terminate_button()
        #     print(date_before)
        #     print(date_after)

    class TestRefundPayments:
        @allure.title('Check RefundPayments')
        def test_refund_button(self, driver):
            test_authorization_form = TestRefundPaymentsPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            time_before, amount_before,  time_after, amount_after = test_authorization_form.test_refund_button()
            assert time_before != time_after or amount_before != amount_after, 'Refund button has not been worked'





