import time

from pages.clients_page import PersonalAccountPage


class TestClients:

    class TestPersonalAccounts:

        def test_sort_personal_ac_kyc(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_kyc_type()
            assert count_before != count_after, 'KYC sort has not been worked'


        def test_sort_personal_ac_citizenship(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_citizenship()
            assert count_before != count_after, 'Citizenship sort has not been worked'
