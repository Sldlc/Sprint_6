from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    FORM_NAME = By.XPATH, "//div[text()='Для кого самокат']"
    NAME = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_SELECTION_LIST = By.XPATH, ".//div[@class='select-search__select']"
    PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"

    # Форма "Про аренду"
    RENT_FORM_NAME = By.XPATH, "//div[text()='Про аренду']"
    DELIVERY_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CALENDAR = By.XPATH, "//div[@class='react-datepicker-popper']"
    CALENDAR_DAY_CHOICE = By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]"
    RENT_PERIOD = By.XPATH, ".//div[text()='* Срок аренды']"
    RENT_PERIOD_LIST = By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='четверо суток']"
    SCOOTER_COLOR_CHECKBOX_GREY = By.XPATH, "//*[@id='grey']"
    SCOOTER_COLOR_CHECKBOX_BLACK = By.XPATH, "//*[@id='black']"
    COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    MAKE_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"
    BACK_BUTTON = By.XPATH, "//button[text()='Назад']"

    # Окно "Хотите оформить заказ?"
    BUTTON_YES = By.XPATH, "//button[text()='Да']"
    BUTTON_NO = By.XPATH, "//button[text()='Нет']"
    BUTTON_CHECK_STATUS = (By.XPATH, ".//*[text()='Посмотреть статус']")
