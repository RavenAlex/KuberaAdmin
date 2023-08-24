from selenium.webdriver.common.by import By


class CurrenciesPageLocators:
    USER_NAME = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                  'Input__left__3GNuo"][name="userName"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                 'Input__left__3GNuo"][name="password"]')
    TWOFACTORAUTH = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                      'Input__left__3GNuo"][name="code2FA"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 '
                                     'Button__medium__2904Q theme-light"]')
    TRANSACTION_TAB = (By.CSS_SELECTOR, 'a[class="Link__link__3Q0IM theme-light Header__navLink__1aP3_"]['
                                        'href="#/transactions"]')
    CURRENCIES_TAB = (By.XPATH, '//*[@id="app"]/div[1]/header/div/div[2]/a[3]')
    CURRENCIES_SEARCH = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]/div')
    CURRENCIES_SEARCH_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]/div/input')
    CURRENCIES_SEARCH_RESULT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td['
                                          '1]/div/div/a')
    CURRENCY_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td['
                                 '1]/div/div/div')
    CURRENCY_DISABLE_CHECK_BOX = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div/div[12]/div['
                                            '2]/div/div/label/span')
    CURRENCY_SAVE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div/div[13]/button')
    CURRENCY_DISABLE_SORT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[2]/div[2]/div')
    CURRENCY_BUTTON_AFTER_DISABLE = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr['
                                               '1]/td[1]/div/div')
    CURRENCY_TRANSPORT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/div/div/div[2]')
    CURRENCY_TRANSPORT_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[3]/table/tbody/tr['
                                           '5]/td[1]')
    TRANSPORT_STATUS_SORT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/div/div/div[1]/div')
    TRANSPORT_STATUS = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[3]/table/tbody/tr[5]/td[5]/div')
    TRANSPORT_STATUS_CHANGE_CHECK_BOX = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[2]/div['
                                                   '2]/div[4]/div/div/label/span')
    TRANSPORT_EDIT_SAVE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/button')
    CURRENCY_TRANSPORT_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[2]/div/div[2]/h3/div/a[3]')
    WITHDRAWAL_CONSTANT_FEE = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[2]/table/tbody/tr['
                                         '1]/td[2]/div/div/div[2]/div/div')
    WITHDRAWAL_CONSTANT_FEE_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div['
                                               '2]/table/tbody/tr[1]/td[2]/div/div/div[2]/div/div/div[1]/input')
    FEES_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[1]/div/div[2]')
    LIMIT_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[1]/div/div[3]')
    TRANSPORT_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[1]/div/div[4]')
    KYC_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[1]/div/div[5]')
    WITHDRAWAL_MINIMUM_LIMIT_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div['
                                                '2]/table/tbody/tr[3]/td[2]/div/div/div[2]/div/div/div/input')
    WITHDRAWAL_MINIMUM_LIMIT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[2]/table/tbody/tr['
                                          '3]/td[2]/div/div/div[2]/div/div')
    DEPOSIT_DURATION_MINUTES = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[2]/table/tbody/tr['
                                          '2]/td[2]/div/div[2]/div[2]/div[1]/div')
    DEPOSIT_DURATION_MINUTES_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div['
                                                '2]/table/tbody/tr[2]/td[2]/div/div[2]/div[2]/div[1]/div/input')
    COUNTRY_CHECK_BOX = (By.CSS_SELECTOR, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div['
                                          '2]/table/tbody/tr/td/div/div/table/tbody/tr[2]/th[1]/div/div/label')
    TRANSPORT_TAB_AFTER = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[2]/div/div[2]/h3/div/a[3]')
    SYSTEM_CLIENTS_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[4]/ul/li[2]/a')
    SYSTEM_CLIENTS_SEARCH = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]')
    SYSTEM_CLIENTS_SEARCH_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]/div['
                                             '1]/input')
    INDRA_WALLETS_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[2]/div[2]/button[1]')
    SAVING_WALLETS_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[2]/div[2]/button[2]')
    UUID_RESULT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[2]/td[2]/div')
    INDRA_WALLETS_ID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/table/tbody/tr[1]/td[2]/div')
    INDRA_TRX_WITHDRAW_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/table/tbody/tr[5]/td['
                                           '3]/div/button')
    INDRA_WITHDRAW_CURRENCY_NAME = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]/div')
    INDRA_WITHDRAW_CURRENCY_AMOUNT = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td['
                                                '3]/div/div[1]/div/div/div')
    INDRA_WITHDRAW_CURRENCY_AMOUNT_FIELD = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td['
                                                      '3]/div/div[1]/div/div/div/div/input')
    INDRA_WITHDRAW_BUTTON_SUBMIT = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/button')
    INDRA_WITHDRAW_AMOUNT_RESULT = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/span[2]')
    INDRA_WITHDRAW_CONFIRM_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/button[2]')
    INDRA_WITHDRAW_SUCCESS = (By.XPATH, '//*[@id="app"]/div[3]/div/span')
    INDRA_SAVING_WALLETS_ID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/table/tbody/tr[1]/td[2]/div')
    INDRA_SAVING_TRX_WITHDRAW_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/table/tbody/tr['
                                                  '4]/td[3]/div/button')
    INDRA_SAVING_WITHDRAW_CURRENCY_NAME = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]/div')
    INDRA_SAVING_WITHDRAW_CURRENCY_AMOUNT = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td['
                                                       '3]/div/div[1]/div/div/div')
    INDRA_SAVING_WITHDRAW_CURRENCY_AMOUNT_FIELD = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div['
                                                             '1]/table/tbody/tr/td[3]/div/div['
                                                             '1]/div/div/div/div/input')
    INDRA_SAVING_WITHDRAW_BUTTON_SUBMIT = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/button')
    INDRA_SAVING_WITHDRAW_AMOUNT_RESULT = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/span[2]')
    INDRA_SAVING_WITHDRAW_CONFIRM_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/button[2]')
    INDRA_SAVING_WITHDRAW_SUCCESS = (By.XPATH, '//*[@id="app"]/div[3]/div/span')
    CLIENTS_WALLET_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[4]/ul/li[3]/a')
    CLIENTS_WALLET_UUID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[6]/div[2]')
    CLIENTS_WALLET_UUID_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[6]/div[2]/div/input')
    CLIENTS_WALLET_OWNER_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr['
                                             '1]/td[7]/div/button')
    CLIENTS_WALLET_OWNER_UUID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/table/tbody/tr[1]/td[2]/div')
    RAVANA_SERVERS_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[4]/ul/li[4]/a')
    RAVANA_SERVER_STATE = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td['
                                     '4]/div/div/label')
    RAVANA_UPDATE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td[5]/div/button')
    RAVANA_UPDATE_STATE_CHECK_BOX = (By.XPATH, '//*[@id="Disabled"]')
    RAVANA_UPDATE_STATE_CHECK_BOX_CONFIRM = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div['
                                                       '5]/div/table/tbody/tr[10]/td/div/button')
    AUDIT_SYSTEM_TAB = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[4]/ul/li[6]/a')
    AUDIT_SYSTEM_BALANCE_UPDATE = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[4]/ul/li[6]/a')




