import allure
from locators.order_page_locators import OrderPageLocators
from page_object.base_page import BasePage
from helpers import *


class OrderPage(BasePage):

    @allure.step('Ввод сгенерированных данных в форму "Для кого самокат" и клик на "Далее"')
    def data_entry_first_form(self):
        self.wait_visibility_of_element(OrderPageLocators.NAME)
        self.click_on_element(OrderPageLocators.NAME)
        self.send_keys_to_input(OrderPageLocators.NAME, name)
        self.click_on_element(OrderPageLocators.SURNAME)
        self.send_keys_to_input(OrderPageLocators.SURNAME, surname)
        self.click_on_element(OrderPageLocators.ADRESS)
        self.send_keys_to_input(OrderPageLocators.ADRESS, adress)
        self.click_on_element(OrderPageLocators.METRO)
        self.send_keys_to_input(OrderPageLocators.METRO, metro)
        self.click_on_element(OrderPageLocators.METRO_SELECTION_LIST)
        self.click_on_element(OrderPageLocators.PHONE)
        self.send_keys_to_input(OrderPageLocators.PHONE, phone_number)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Ввод сгенерированных данных в форму "Про аренду" и клик на "Посмотреть статус заказа"')
    def data_entry_second_form(self):
        self.wait_visibility_of_element(OrderPageLocators.DELIVERY_DATE)
        self.click_on_element(OrderPageLocators.DELIVERY_DATE)
        self.send_keys_to_input(OrderPageLocators.DELIVERY_DATE, date)
        self.click_on_element(OrderPageLocators.SCOOTER_COLOR_CHECKBOX_GREY)
        self.click_on_element(OrderPageLocators.SCOOTER_COLOR_CHECKBOX_BLACK)
        self.click_on_element(OrderPageLocators.RENT_PERIOD)
        self.click_on_element(OrderPageLocators.RENT_PERIOD_LIST)
        self.click_on_element(OrderPageLocators.COMMENT)
        self.send_keys_to_input(OrderPageLocators.COMMENT, comment)
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.wait_visibility_of_element(OrderPageLocators.BUTTON_YES)
        self.click_on_element(OrderPageLocators.BUTTON_YES)
        self.wait_visibility_of_element(OrderPageLocators.BUTTON_CHECK_STATUS)

    @allure.step('Выбор станции метро из выпадающего списка')
    def select_metro_station(self):
        self.click_on_element(OrderPageLocators.METRO_SELECTION_LIST)

    @allure.step('Ввод даты заказа в поле "Когда привезти самокат"')
    def select_date(self):
        self.send_keys_to_input(OrderPageLocators.DELIVERY_DATE).send_keys(date)

    @allure.step('Выбор даты в выпадающем календаре поля начала аренды')
    def choose_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.CALENDAR_DAY_CHOICE)

    @allure.step('Отображение кнопки "Посмотреть статус" после создания заказа')
    def check_status_button_is_displaying(self):
        return self.check_displaying_of_element(OrderPageLocators.BUTTON_CHECK_STATUS)
