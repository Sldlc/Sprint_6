import allure
import pytest
from page_object.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from conftest import driver


class TestOrderPageOrder:
    @allure.title('Проверка возможности оформить заказ Самоката')
    @allure.description('Наборы тестов проверяющие успешное оформление заказа с главной страницы и хедэра')
    @pytest.mark.parametrize('order_button', [(MainPageLocators.HEADER_ORDER_BUTTON),
                                              (MainPageLocators.MAIN_ORDER_BUTTON)])
    def test_order_all_fields_success(self, driver, order_button):
        order_page = OrderPage(driver)
        order_page.scroll_to_faq(order_button)
        order_page.wait_visibility_of_element(order_button)
        order_page.click_on_element(order_button)
        order_page.data_entry_first_form()
        order_page.data_entry_second_form()
        assert order_page.check_status_button_is_displaying()
