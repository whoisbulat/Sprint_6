import pytest
from pages.main_page import MainPageHelper
from pages.order_page import OrderPageHelper
from data import UserData


class TestOrder:
    @pytest.mark.parametrize('first_name, last_name, adress, phone, data, comment', UserData.user_data_1 + UserData.user_data_2)

    def test_success_order_from_profile_header_button_with_only_required_fields(self, driver, first_name, last_name, adress, phone, data, comment):
        main_page = MainPageHelper(driver)
        order_page = OrderPageHelper(driver)
        main_page.go_to_site()
        main_page.close_cookie()
        main_page.click_on_order_batton_on_hedder()
        order_page.create_order(first_name, last_name, adress, phone, data, comment)
        assert 'Заказ оформлен' in order_page.check_success_order()

    def test_order_page_transition_from_bottom_button(self, driver):
        main_page = MainPageHelper(driver)
        order_page = OrderPageHelper(driver)
        main_page.go_to_site()
        main_page.close_cookie()
        main_page.click_on_order_batton_on_content()
        assert 'Для кого самокат' in order_page.check_order_page_transition()
