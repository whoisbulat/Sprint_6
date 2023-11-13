from pages.base_page import BasePage
from pages.main_page import MainPageHelper
import time
from conftest import driver

class TestLogo:
    def test_yandex_logo_redirects_to_dzen_main_page(self, driver):
        base_page = BasePage(driver)
        main_page = MainPageHelper(driver)
        base_page.go_to_site()
        main_page.click_on_yandex_LOGO()
        base_page.check_last_open_window()
        time.sleep(5)
        assert base_page.get_current_url() == 'https://dzen.ru/?yredirect=true'

    def test_Scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPageHelper(driver)
        base_page = BasePage(driver)
        base_page.go_to_site()
        main_page.click_on_order_batton_on_hedder()
        main_page.click_on_Scooter_LOGO()
        main_text_on_main = main_page.find_home_header()
        assert 'Самокат' in main_text_on_main.strip()
