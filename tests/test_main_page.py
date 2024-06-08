import allure
import pytest
from page_object.main_page import MainPage
from conftest import driver
from data import *


class TestMainPage:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('При нажатии на вопрос должен открываться текст ответа')
    @pytest.mark.parametrize('num, result', [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f), (6, g), (7, h)])
    def test_click_faq_expand_icons_text_is_expected(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        assert main_page.get_answer_text(num) == result
