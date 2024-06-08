import allure
from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Подождать прогрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Подождать прогрузки части лого с надписью "Яндекс" в хэдере')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.HEADER_YANDEX_LOGO)

    @allure.step('Подождать прогрузки части лого с надписью "Самокат" в хэдере')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.HEADER_SCOOTER_LOGO)

    @allure.step('Кликнуть по части лого с надписью "Яндекс" в хэдере')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.HEADER_YANDEX_LOGO)

    @allure.step('Кликнуть по части лого с надписью "Самокат" в хэдере')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.HEADER_SCOOTER_LOGO)

    @allure.step('Подождать прогрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.SITE_HEADER)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.SITE_HEADER)

    @allure.step('Проскроллить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_faq(MainPageLocators.FAQ_SECTION)

    # thinking
    @allure.step('Подождать прогрузки нужного номера вопроса в аккордеоне "Вопросы о важнoм"')
    def wait_visibility_of_faq_items(self, num):
        self.wait_visibility_of_element(MainPageLocators.FAQ_QUESTION)

    @allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важнoм"')
    def click_on_faq_items(self, num):
        self.click_on_element(MainPageLocators.FAQ_QUESTION)

    @allure.step('Подождать прогрузки нужного номера ответа в аккордеоне "Вопросы о важнoм"')
    def wait_visibility_of_faq_answer(self, num):
        self.wait_visibility_of_element(MainPageLocators.FAQ_ANSWER)

    @allure.step('Получение текста ответа')
    def get_displayed_text_from_faq_answer(self, num):
        return self.get_text_on_element(MainPageLocators.FAQ_ANSWER)

    def get_answer_text(self, num):
        locator_q_formated = self.format_locators(MainPageLocators.FAQ_QUESTION, num)
        locator_a_formated = self.format_locators(MainPageLocators.FAQ_ANSWER, num)
        self.click_on_element(locator_q_formated)
        return self.get_text_from_element(locator_a_formated)
