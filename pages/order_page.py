import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class OrderPageLocators:
    LOCATOR_NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    LOCATOR_LASTNAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    LOCATOR_ADRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    LOCATOR_METRO_INPUT = By.CLASS_NAME, "select-search"
    LOCATOR_METRO_DROP = By.XPATH, "//div[contains(text(),'Сокольники')]"
    LOCATOR_PHONE_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    LOCATOR_NEXT_BATTON = By.XPATH, "//button[contains(text(),'Далее')]"
    LOCATOR_DATA_INPUT = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    LOCATOR_RENT_PERIOD_INPUT = By.XPATH, "//div[contains(text(),'* Срок аренды')]"
    LOCATOR_DROP_DOWN_RENT_PERIOD = By.XPATH, "//div[contains(text(),'сутки')]"
    LOCATOR_COLOR_SCOOTER_BLACK = By.XPATH, "//input[@id='black']"
    LOCATOR_COMMENT_INPUT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    LOCATOR_ORDER_BATTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    LOCATOR_YES_BATTON_ON_CONFIRM_MODAL = By.XPATH, "//button[contains(text(),'Да')]"
    LOCATOR_ORDER_MODAL = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"
    LOCATOR_LABEL_ON_ORDER_PAGE = By.XPATH, "//div[contains(text(), 'Для кого самокат')]"



class OrderPageHelper(BasePage):

    @allure.step('Заполняем поле имя')
    def set_name_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LOCATOR_NAME_INPUT, text)

    @allure.step('Заполняем поле фамилия')
    def set_lastname_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LOCATOR_LASTNAME_INPUT, text)

    @allure.step('Заполняем поле адрес')
    def set_adress_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LOCATOR_ADRESS_INPUT, text)

    @allure.step('Заполняем поле метро')
    def set_metro_to_field(self):
        self.click_to_element(OrderPageLocators.LOCATOR_METRO_INPUT)
        self.click_to_element(OrderPageLocators.LOCATOR_METRO_DROP)

    @allure.step('Заполняем поле телефон')
    def set_phone_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LOCATOR_PHONE_INPUT, text)

    @allure.step('кликаем на кнопку далее')
    def click_to_continue_batton(self):
        self.click_to_element(OrderPageLocators.LOCATOR_NEXT_BATTON)

    @allure.step('заполняем поле дата')
    def set_data_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LOCATOR_DATA_INPUT, text)

    @allure.step('Заполняем поле срок аренды')
    def set_rent_period_to_field(self):
        self.click_to_element(OrderPageLocators.LOCATOR_RENT_PERIOD_INPUT)
        self.click_to_element(OrderPageLocators.LOCATOR_DROP_DOWN_RENT_PERIOD)

    @allure.step('Выбираем черный цвет самоката. Необязательное поле')
    def set_check_box_color_vlack(self):
        self.click_to_element(OrderPageLocators.LOCATOR_COLOR_SCOOTER_BLACK)

    @allure.step('заполняем комментарий для курьера')
    def set_comment_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LOCATOR_COMMENT_INPUT, text)

    @allure.step('Нажмимаем на кнопку заказа')
    def click_order_batton(self):
        self.click_to_element(OrderPageLocators.LOCATOR_ORDER_BATTON)

    @allure.step('Кликаем "да" в сплывающем окне подтверждения заказа')
    def click_yes_on_batton_in_confirm_modal(self):
        self.click_to_element(OrderPageLocators.LOCATOR_YES_BATTON_ON_CONFIRM_MODAL)

    @allure.step('Проверяем, что заказ оформился и появилось всплывающее окно')
    def check_success_order(self):
        order_modal = self.find_element(OrderPageLocators.LOCATOR_ORDER_MODAL)
        return order_modal.text

    @allure.step('Проверяем, что открылась страница заказа')
    def check_order_page_transition(self):
        main_text_in_order_page = self.find_element(OrderPageLocators.LOCATOR_LABEL_ON_ORDER_PAGE)
        return main_text_in_order_page.text


    def create_order(self, first_name, last_name, adress, phone,data,comment):
        self.set_name_to_field(first_name)
        self.set_lastname_to_field(last_name)
        self.set_adress_to_field(adress)
        self.set_metro_to_field()
        self.set_phone_to_field(phone)
        self.click_to_continue_batton()
        self.set_data_to_field(data)
        self.set_check_box_color_vlack()
        self.set_rent_period_to_field()
        self.set_comment_to_field(comment)
        self.click_order_batton()
        self.click_yes_on_batton_in_confirm_modal()

