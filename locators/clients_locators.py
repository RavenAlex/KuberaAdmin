from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
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
    CLIENTS_BUTTON = (By.CSS_SELECTOR, 'a[class="Link__link__3Q0IM theme-light Header__navLink__1aP3_"]['
                                       'href="#/clients"]')
    COUNT = (By.CSS_SELECTOR, 'div[class="Text__subtitle-normal__31PIJ Text__brand__2B2cJ theme-light"]')
    KYC_TYPE = (By.CSS_SELECTOR, 'div[class="Select__control__3OleG theme-light control--is-focused '
                                 'PersonalAccounts__citizenshipCombobox__1y6d_"]')
    KYC_TYPE_FIELD = (By.XPATH, '//*[@id="react-select-7-input"]')
    KYC_RESIDENT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]/div')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 '
                                      'Button__large__W2P3N theme-light"]')
    CITIZENSHIP_COUNTRY = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[3]/div[2]/div')
    PRODUCT_ID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[4]/div[2]/div')
    START_DATE_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/div[1]/div[2]/div/div/input')
    END_DATE_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/div[2]/div[2]/div/div/input')
    START_DATE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/div[1]/div[2]/div/div')
    END_DATE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/div[2]/div[2]/div/div')
    SEARCH_EON_ID_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[1]')
    SEARCH_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/form/div[1]/div/div/input')
    EON_ID_CLIENT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[5]/table/tbody/a/div/div[1]/div[2]')
    CLIENT_UUID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/table/tbody/tr[1]/td[2]/div')
    KYC_ORDERS = (By.CSS_SELECTOR, 'a[class="Link__link__3Q0IM theme-light SideNavMenu__link__2IdQq theme-light"]['
                                   'href="#/clients/orders"]')
    START_ORDER_DATE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div/div/div')
    END_ORDER_DATE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[2]/div/div/div')
    START_ORDER_DATE_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div/div/div/input')
    END_ORDER_DATE_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[2]/div/div/div/input')
    GO_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 Button__large__W2P3N '
                                  'OrdersTable__button__3I6SB theme-light"]')
    RESULT_ORDER_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/a')
    ORDER_ID = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]')
    CLOSE_ORDER_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[1]')
    GET_REPORT_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 '
                                          'Button__medium__2904Q theme-light"]')
    REPORT_FROM_DATE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div/div')
    REPORT_FROM_DATE = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div/div/input')
    REPORT_TO_DATE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/div[2]/div/div')
    REPORT_TO_DATE = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/div[2]/div/div/input')
    EMPTY_PLACE = (By.XPATH, '/html/body/div[2]/div/div[2]/h6')
    REPORT_FINAL_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 '
                                            'Button__large__W2P3N theme-light"]')
    RESULT_OF_REPORT = (By.XPATH, '//*[@id="app"]/div[3]/div/span')
    ORGANIZATION = (By.CSS_SELECTOR, 'a[href="#/clients/organizations"]')
    ORGANIZATION_SEARCH = (By.CSS_SELECTOR, 'div[class="theme-light Input__inputContainer__3ik5u '
                                                   'Input__medium__wJu2O"]')
    ORGANIZATION_SEARCH_INPUT = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O '
                                                  'Input__left__3GNuo"]')
    ORGANIZATION_SEARCH_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/form/div[2]/button')
    ORGANIZATION_SEARCH_CLICK = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/div/table/tbody/tr/td[2]/div')
    ORGANIZATION_SEARCH_RESULT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div/div/table/tbody/tr/td['
                                            '1]/div')
    ORGANIZATION_SEARCH_UUID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[5]/div/table/tbody/tr['
                                          '1]/td[2]/div/div/div/input')
    LIST_OF_DETAILS = (By.CSS_SELECTOR, 'a[href="#/clients/list-details"]')
    ACCOUNT_ID = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]')
    ACCOUNT_ID_FIELD = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O Input__left__3GNuo"]')
    APPLY_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 Button__large__W2P3N '
                                     'theme-light"]')
    UUID_DETAILS_RESULT = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div')
    DETAILS_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td[7]/div/button')
    ACCOUNT_ID_LIST_OF_DETAILS = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td[2]/div')
    TRANSPORT_ID_RESULT_TABLE = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div')
    TRANSPORT_ID_RESULT_DETAILS = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div/table/tbody/tr[1]/td[2]/div')
    LIST_OF_QUESTIONNAIRES = (By.CSS_SELECTOR, 'a[href="#/clients/list-questionnaries"]')
    ORDER_ID_OF_QUESTIONNAIRES = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[7]/td[1]/div')
    INFO_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[2]/table/tbody/tr[7]/td[7]/div/button')
    REASON_AREA = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[5]/table/tbody/tr[1]/td/div/textarea')
    APPROVE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[5]/table/tbody/tr[2]/td/div/div/button[2]')
    CLOSE_QUESTIONNAIRE_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[6]/button[2]')
    COUNTRY_SETTING = (By.CSS_SELECTOR, 'a[href="#/clients/saraswati"]')
    COUNTRY_SEARCH_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/main/section/div/div[5]/div[1]/div[1]/div[2]')
    COUNTRY_SEARCH_INPUT = (By.CSS_SELECTOR, 'input[class="theme-light Input__input__2H4nT Input__medium__wJu2O Input__left__3GNuo"]')
    COUNTRY_SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 Button__large__W2P3N theme-light"]')
    COUNTRY_EDIT = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 Button__medium__2904Q Saraswati__rowButton__1o_sd theme-light"]')
    COUNTRY_ALLOWED_CHECK_BOX = (By.XPATH, '/html/body/div[2]/div/div[3]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/div')
    COUNTRY_EDIT_SAVE = (By.CSS_SELECTOR, 'button[class="Button__button__1O1uA Button__primary__3QLI9 Button__medium__2904Q theme-light"]')
    COUNTRY_EDIT_CLOSE = (By.XPATH, '/html/body/div[2]/div/div[1]')
