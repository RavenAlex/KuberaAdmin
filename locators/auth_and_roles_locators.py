from selenium.webdriver.common.by import By
import random


class AuthAndRolePageLocators:
    USER_NAME = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                  'Input__left__3GNuo"][name="userName"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                 'Input__left__3GNuo"][name="password"]')
    TWOFACTORAUTH = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                      'Input__left__3GNuo"][name="code2FA"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 '
                                     'Button__medium__2904Q theme-light"]')
    KADM_MENU = (By.CSS_SELECTOR, 'div[class="Grid__item__2TpG8 Grid__item-8__Ow6fv '
                                  'Header__headerGridLinksContainer__1W0u_"]')


class TransactionSearchLocators:
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
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                     'Input__left__3GNuo"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 '
                                      'Button__large__W2P3N theme-light"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'tbody[class="Table__tbody__1ssLt"]')
    PAYMENT_ID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/section[1]/div/table/tbody/tr[1]/td['
                            '2]/div/td/div')
    TRANSPORT_ID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/section[1]/div/table/tbody/tr[8]/td['
                              '2]/div/td/div')
    AMOUNT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/section[1]/div/table/tbody/tr[3]/td['
                        '2]/div/td/div')
    RECIPIENT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/section[5]/div/table/tbody/tr[1]/td['
                           '2]/div/td/div')


class TestSecurityManagerPageLocators:
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
    SECURITY_MANAGER = (By.CSS_SELECTOR, 'a[class="Link__link__3Q0IM theme-light SideNavMenu__link__2IdQq '
                                         'theme-light"][href="#/transactions/security"]')
    PRODUCT_SORT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]/div/div[1]/div[1]')
    PRODUCT_SORT_FIELD = (By.CSS_SELECTOR, 'input[id="react-select-5-input"]')
    TOTAL_COUNT = (By.CSS_SELECTOR, 'div[class="Text__primary__9os-D BBTable__totalCount__3y6A1 theme-light"]')
    TRANSACTION_SORT = (By.CSS_SELECTOR, 'input[id="react-select-6-input"]')


