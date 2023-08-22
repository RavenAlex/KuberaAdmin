import time

import allure

from pages.currencies_page import CurrenciesPage


class TestCurrencies:
    class TestCurrencyManagement:
        def test_currencies(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            search_result = test_currencies.currency_management_search()
            assert search_result == 'BTC', 'Search has not been worked or BTC is disable'

        def test_disable_currencies(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            search_result = test_currencies.disable_currencies()
            assert search_result == 'BTC', 'Сurrency switch not working'

        def test_edit_transport(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            transport_status_before, transport_status_after, withdrawal_constant_fee_before, \
            withdrawal_constant_fee_after, withdrawal_minimum_amount_before, withdrawal_minimum_amount_after, \
            deposit_duration_minutes_before, deposit_duration_minutes_after = test_currencies.edit_transport()
            assert transport_status_before != transport_status_after and withdrawal_constant_fee_before != \
                   withdrawal_constant_fee_after and withdrawal_minimum_amount_before != withdrawal_minimum_amount_after\
                   and deposit_duration_minutes_before != deposit_duration_minutes_after, 'Edit transport has not been worked'
