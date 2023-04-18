import time
from pages.authorize_and_roles_page import AuthAndRolePage, TransactionSearchPage


class TestForm:

    class TestAuthAndRoles:

        def test_auth(self, driver):
            test_authorization_form = AuthAndRolePage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            super_admin = test_authorization_form.auth_superadmin_role_int()
            assert super_admin == 'TRANSACTIONSCLIENTSCURRENCIESEXCHANGERPRODUCTSCMSSWAPADMINMERCHANTSBEST ' \
                                  'BARTERINVESTMENTSSARASWATI', 'Authorization has not been worked or super admin ' \
                                                                'menu incorrect displayed '

    class TestTransaction:

        def test_transaction_search(self, driver):
            test_authorization_form = TransactionSearchPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            test_authorization_form.auth_superadmin_int()
            transaction_result = test_authorization_form.search_transaction()
            transaction_attachment = test_authorization_form.results_attachment()
            assert transaction_result == "['98074', 'EON-AEN4T-L6G5U-GJR7W', " \
                                         "'RAVANA:EON-int=DEPOSITORY:int=ColorCoin=BTC', '0.0001'] ", 'Transaction ' \
                                                            'value incorrect display in table or search does not work'
            assert transaction_result == transaction_attachment, 'Transaction attachment has not been opened ' \
                                                                 'or value bot correct'

