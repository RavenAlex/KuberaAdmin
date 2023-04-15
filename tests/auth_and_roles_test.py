import time
from pages.authorize_and_roles_page import AuthAndRolePage


class TestForm:

    class TestAuthAndRoles:

        def test_auth(self, driver):
            test_authorization_form = AuthAndRolePage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_authorization_form.open()
            super_admin = test_authorization_form.auth_superadmin_role_int()
            assert super_admin == 'TRANSACTIONSCLIENTSCURRENCIESEXCHANGERPRODUCTSCMSSWAPADMINMERCHANTSBEST ' \
                                  'BARTERINVESTMENTSSARASWATI', 'Authorization has not been worked or super admin ' \
                                                                'menu incorrect displayed '

