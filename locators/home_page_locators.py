from selenium.webdriver.common.by import By


class HomePageLocators: # локаторы для элементов главной страницы
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']/img[@alt='Yandex']") # логотип Яндекса
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']/img[@alt='Scooter']") # логотип Самоката
