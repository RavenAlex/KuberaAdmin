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


        def test_sort_product_id(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_product_id()
            assert count_before != count_after, 'Product ID sort has not been worked'

        def test_sort_date(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_date()
            assert count_before != count_after and count_after == '116', 'Date sort has not been worked'

        def test_search_eon_id(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            client_uuid = test_sort_personal.search_eon_id()
            assert client_uuid == '29b27394-ea52-4190-b4dd-93b88db78ebe', 'Search by eon id gas not been worked'


