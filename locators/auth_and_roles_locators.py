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
    TYPE_SORT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[1]')
    TYPE_SORT_FIELD = (By.CSS_SELECTOR, 'input[id="react-select-6-input"]')
    SECURITY_TRANSACTION = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr['
                                             '4]/td[1]')
    DATE_PICKER_IN_LIST = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[4]/td['
                                     '7]/div/a/div')
    REJECT_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__secondary__26O0b '
                                      'Button__medium__2904Q PaymentResolutionControls__button__3TFOT theme-light"]')
    REJECT_REASON = (By.CSS_SELECTOR, 'textarea[class="theme-light TextArea__input__1ZnS6 FieldText__textarea__3P20h"]')
    APPROVE_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 '
                                       'Button__medium__2904Q PaymentResolutionControls__button__3TFOT theme-light"]')
    SINGLE_APPROVE_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__secondary__26O0b '
                                              'Button__medium__2904Q theme-light"]')

class TestActivePaymentsPageLocators:
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
    ACTIVE_PAYMENTS = (By.CSS_SELECTOR, 'a[class="Link__link__3Q0IM theme-light SideNavMenu__link__2IdQq theme-light"][href="#/transactions/active"]')
    ACTIVE_COUNT = (By.CSS_SELECTOR, 'div[class="Text__primary__9os-D BBTable__totalCount__3y6A1 theme-light"]')
    ACTIVE_PAYMENTS_SORT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div/div')
    SELECT_MENU = (By.CSS_SELECTOR, 'div[class="Select__menuList__1lKQX theme-light Combobox__menu-list css-13ad1he"]')
    TIME_ACTIVE_TRANSACTION = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[10]/td[8]/div/a/div')
    ACTIVE_TRANSACTION = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[10]/td[1]')
    TERMINATE_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 Button__small__u3ywy theme-light"]')
    TERMINATE_RETURN = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__outline__3keiv Button__medium__2904Q PaymentContainer__buttonReturn__1lg3c theme-light"]')


class TestRefundPaymentsPageLocators:
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
    REFUND_PAYMENTS = (By.CSS_SELECTOR, 'a[class="Link__link__3Q0IM theme-light SideNavMenu__link__2IdQq theme-light"][href="#/transactions/refund"]')
    REFUND_TIME = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/table/tbody/tr[1]/td[5]/div')
    REFUND_AMOUNT_EUR = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/table/tbody/tr[1]/td[4]/div')
    REFUND_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/table/tbody/tr[1]/td[6]/div/button')
