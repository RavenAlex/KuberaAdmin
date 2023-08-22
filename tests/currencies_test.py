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
            print(search_result)
