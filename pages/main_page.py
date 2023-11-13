from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class MainPageLocators:
    LOCATOR_ORDER_BATTON_ON_HEDDER = By.CLASS_NAME, "Button_Button__ra12g"
    LOCATOR_ORDER_BTN_ON_CONTENT = By.CLASS_NAME, "Home_FinishButton__1_cWm"
    LOCATOR_YANDEX_LOGO = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    LOCATOR_Scooter_LOGO = By.CLASS_NAME, "Header_LogoScooter__3lsAR"
    LOCATOR_QUESTION = By.XPATH, "//div[@id='accordion__heading-{}']"
    LOCATOR_ANSWER =  By.XPATH, "//div[@id='accordion__panel-{}']"
    LOCATOR_COOKIE = By.CLASS_NAME, "App_CookieButton__3cvqF"
    LOCATOR_HOME_STATUS = By.CLASS_NAME, "Home_Header__iJKdX"


class MainPageHelper(BasePage):

    def get_question(self, num):
        method, locator = MainPageLocators.LOCATOR_QUESTION
        locator = locator.format(num)
        self.find_element((method, locator))
        self.scroll_to_element((method, locator))
        self.click_to_element((method, locator))

    def get_answer(self, num):
        method, locator = MainPageLocators.LOCATOR_ANSWER
        locator = locator.format(num)
        answer = self.find_element((method, locator))
        return answer.text

    def click_on_Scooter_LOGO(self):
        self.click_to_element(MainPageLocators.LOCATOR_Scooter_LOGO)


    def click_on_yandex_LOGO(self):
        self.click_to_element(MainPageLocators.LOCATOR_YANDEX_LOGO)

    def click_on_order_batton_on_hedder(self):
        self.click_to_element(MainPageLocators.LOCATOR_ORDER_BATTON_ON_HEDDER)

    def click_on_order_batton_on_content(self):
        self.find_element(MainPageLocators.LOCATOR_ORDER_BTN_ON_CONTENT)
        self.scroll_to_element(MainPageLocators.LOCATOR_ORDER_BTN_ON_CONTENT)
        self.click_to_element(MainPageLocators.LOCATOR_ORDER_BTN_ON_CONTENT)

    def find_home_header(self):
        home_header = self.find_element(MainPageLocators.LOCATOR_HOME_STATUS)
        return home_header.text

    def close_cookie(self):
        self.click_to_element(MainPageLocators.LOCATOR_COOKIE)





