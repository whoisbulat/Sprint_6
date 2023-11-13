import pytest

from pages.base_page import BasePage
from pages.main_page import MainPageHelper
from pages.order_page import OrderPageHelper

import time


class TestOrder:
    @pytest.mark.parametrize('first_name, last_name, adress, phone, data, comment',
                             [("Булат", "Ибрагимов", "Адрес дома 2", "89273345673", "18.11.2023",
                               "Как сказать девушке что она не права чтобы это не привело к ссоре?"),
                              ("Имя", "Фамилия", "Адрес 2", "+9283349324", "25.11.2023",
                               "коммент курьеру")
                              ])
    def test_success_order_from_profile_header_button_with_only_required_fields(self, driver, first_name, last_name, adress, phone, data, comment):
        base_page = BasePage(driver)
        main_page = MainPageHelper(driver)
        order_page = OrderPageHelper(driver)
        base_page.go_to_site()
        main_page.close_cookie()
        main_page.click_on_order_batton_on_hedder()
        order_page.create_order(first_name, last_name, adress, phone, data, comment)
        assert 'Заказ оформлен' in order_page.check_success_order()

    def test_order_page_transition_from_bottom_button(self, driver):
        base_page = BasePage(driver)
        main_page = MainPageHelper(driver)
        base_page.go_to_site()
        main_page.close_cookie()
        main_page.click_on_order_batton_on_content()