import time

import allure

from pages.clients_page import PersonalAccountPage

@allure.suite("Clients")
class TestClients:
    @allure.feature('PersonalAccounts')
    class TestPersonalAccounts:
        @allure.title('Check Sort personal account KYC')
        def test_sort_personal_ac_kyc(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_kyc_type()
            assert count_before != count_after, 'KYC sort has not been worked'

        @allure.title('Check Sort personal account citizenship')
        def test_sort_personal_ac_citizenship(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_citizenship()
            assert count_before != count_after, 'Citizenship sort has not been worked'

        @allure.title('Check Sort priduct ID')
        def test_sort_product_id(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_product_id()
            assert count_before != count_after, 'Product ID sort has not been worked'

        @allure.title('Check Sort date')
        def test_sort_date(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            count_before, count_after = test_sort_personal.sort_date()
            assert count_before != count_after and count_after == '116', 'Date sort has not been worked'

        @allure.title('Check search EON-ID')
        def test_search_eon_id(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            client_uuid = test_sort_personal.search_eon_id()
            assert client_uuid == '29b27394-ea52-4190-b4dd-93b88db78ebe', 'Search by eon id gas not been worked'

        @allure.title('Check KYC orders')
        def test_kyc_orders(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            kyc_orders_result = test_sort_personal.kyc_orders()
            assert kyc_orders_result == '548e95bb-910a-4924-aced-164025b900b7', 'KYC orders sort by date has not been ' \
                                                                                'worked '

        @allure.title('Check KYC orders report')
        def test_kyc_orders_report(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            result_of_report = test_sort_personal.kyc_orders_report()
            assert result_of_report == 'Success', 'Report has not been downloaded'

        @allure.title('Check organisation main')
        def test_organisation_main(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            search_result, result_uuid = test_sort_personal.organisation_main()
            search_result == result_uuid, 'Search and enter in organization has not been working'

        @allure.title('Check list of details')
        def test_list_of_details(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            result_table, result_detail = test_sort_personal.list_of_details_sort()
            assert result_table == 'EON-PBZER-9YGNB-P46MM' and result_table == result_detail, 'List of details has ' \
                                                                                              'not been correct worked '

        @allure.title('Check list of questionnaire')
        def test_list_of_questionnaire(self, driver):
            test_sort_personal = PersonalAccountPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_sort_personal.open()
            test_sort_personal.auth_superadmin_int()
            time.sleep(1)
            order_id_before, order_id_after = test_sort_personal.list_of_questionnaire()
            assert order_id_before != order_id_after, 'Questionnaire approve has not been worked'




