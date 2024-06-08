import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл')
    def scroll_to_faq(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание загрузки элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод значения в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Перевключение на новое окно')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_text_from_element(self, locator):
        return self.wait_visibility_of_element(locator).text

    @allure.step('форматирование локаторов')
    def format_locators(self, locator_1, num):
        method, locator = locator_1    # By.XPATH, '//div[@id="accordion__heading-{}"]/parent::div'
        locator = locator.format(num)  # By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'
        return method, locator

    @allure.step('Получить заголовок страницы')
    def get_page_title(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.title
