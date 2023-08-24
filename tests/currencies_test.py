import time

import allure

from pages.currencies_page import CurrenciesPage

@allure.suite("Currencies")
class TestCurrencies:
    @allure.feature('CurrencyManagement')
    class TestCurrencyManagement:
        @allure.title('Check search currency')
        def test_currencies(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            search_result = test_currencies.currency_management_search()
            assert search_result == 'BTC', 'Search has not been worked or BTC is disable'

        @allure.title('Check disable currency')
        def test_disable_currencies(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            search_result = test_currencies.disable_currencies()
            assert search_result == 'BTC', 'Сurrency switch not working'

        @allure.title('Check edit transport')
        def test_edit_transport(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            transport_status_before, transport_status_after, withdrawal_constant_fee_before, \
            withdrawal_constant_fee_after, withdrawal_minimum_amount_before, withdrawal_minimum_amount_after, \
            deposit_duration_minutes_before, deposit_duration_minutes_after = test_currencies.edit_transport()
            assert transport_status_before != transport_status_after and withdrawal_constant_fee_before != \
                   withdrawal_constant_fee_after and withdrawal_minimum_amount_before != withdrawal_minimum_amount_after \
                   and deposit_duration_minutes_before != deposit_duration_minutes_after, 'Edit transport has not been worked'

    @allure.feature('SystemClients')
    class TestSystemClients:
        @allure.title('Check system clients search')
        def test_system_clients_search(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            search_result = test_currencies.system_clients_search()
            assert search_result == 'BEST_BARTER:int', 'System clients search has not been worked'

        @allure.title('Check indra wallets withdraw')
        def test_indra_wallets_withdraw(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            indra_wallet_id, indra_withdraw_name_currency, indra_withdraw_amount_result, \
            indra_withdraw_success = test_currencies.indra_wallets_withdraw()
            assert indra_wallet_id == 'EON-JTTX6-QH6D4-EHYPX' and indra_withdraw_name_currency == 'TRX' \
                   and indra_withdraw_amount_result == '10 TRX' and indra_withdraw_success == 'Success', \
                   'Indra waletts withdraw has not been worked'

        @allure.title('Check indra saving wallets withdraw')
        def test_indra_savings_wallets_withdraw(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            indra_saving_wallet_id, indra_saving_withdraw_name_currency, indra_saving_withdraw_amount_result, \
            indra_saving_withdraw_success = test_currencies.indra_saving_wallets_withdraw()
            assert indra_saving_wallet_id == 'EON-2BCJR-P7UQH-3U9NK' and indra_saving_withdraw_name_currency == 'TRX' \
                   and indra_saving_withdraw_amount_result == '1 TRX' and indra_saving_withdraw_success == 'Success', \
                    'Indra saving withdraw has not been worked'

    @allure.feature('ClientsWallets')
    class TestSystemClients:
        @allure.title('Check clients wallets owner')
        def test_clients_wallets_owner(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            test_currencies.clients_wallets_owner()

    @allure.feature('RavanaServers')
    class TestSystemClients:
        @allure.title('Check disable ravana server')
        def test_ravana_server(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            state = test_currencies.ravana_servers()
            assert state == 'Checkbox__checkbox__32K2t Checkbox__small__oZRCx Checkbox__disabled__30R8E ' \
                            'theme-light', 'Ravana servers disabled has not been worked'

    @allure.feature('AuditSystem')
    class TestSystemClients:
        @allure.title('Check audit system balance update')
        def test_audit_system_balance_update(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            test_currencies.audit_system_balance_update()

        @allure.title('Check audit system balance ravana withdraw')
        def test_audit_system_balance_ravana_withdraw(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            audit_ravana_withdraw_result = test_currencies.audit_system_balance_ravana_withdraw()
            assert audit_ravana_withdraw_result == 'Success', 'Balance Ravana withdraw has not been worked'

        @allure.title('Check audit system allocation funds sort')
        def test_audit_system_allocation_funds_sort(self, driver):
            test_currencies = CurrenciesPage(driver, 'https://kadm.int.exscudo.com/#/signin')
            test_currencies.open()
            test_currencies.currencies_button()
            time.sleep(1)
            state_one, state_two = test_currencies.audit_system_allocation_funds_sort()
            assert state_one == 'ALLOCATED' and state_two == 'RELEASED', 'Sort of allocation funds has not been worked'







