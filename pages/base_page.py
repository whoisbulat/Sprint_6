from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self,locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def check_last_open_window(self):
        WebDriverWait(self.driver, 10).until(EC.url_changes)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)





