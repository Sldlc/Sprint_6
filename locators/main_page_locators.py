from selenium.webdriver.common.by import By


class MainPageLocators:
    # FAQ
    FAQ_SECTION = By.XPATH, '//div[contains(@class, "Home_FAQ")]'
    FAQ_QUESTION = By.XPATH, '//div[@id="accordion__heading-{}"]/parent::div'
    FAQ_ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]'

    # Main page
    SITE_HEADER = By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]'
    MAIN_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    HEADER_ORDER_BUTTON = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    # Logo
    HEADER_SCOOTER_LOGO = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    HEADER_YANDEX_LOGO = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    TITLE = (By.TAG_NAME, 'title')
