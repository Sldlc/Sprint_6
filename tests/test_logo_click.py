import allure
from conftest import driver
from page_object.main_page import MainPage
from locators.main_page_locators import *


class TestLogoRedirect:
    @allure.title('При нажатии на логотип «Самокат», идет переход на главную страницу Самоката')
    def test_logo_samokat_navigate_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('При нажатии на логотип «Яндекс», идет переход на страницу Дзен')
    def test_logo_yandex_navigate_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_new_tab()
        assert main_page.get_page_title(MainPageLocators.TITLE) == 'Дзен'
