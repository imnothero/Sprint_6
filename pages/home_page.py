import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class HomePage(BasePage): 
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Клик на логотип Яндекса")  
    def click_yandex_logo(self):
        yandex_logo = self.wait.until(EC.element_to_be_clickable(HomePageLocators.YANDEX_LOGO))
        yandex_logo.click()  
        self.wait_for_new_window()  

    @allure.step("Клик на логотип Самоката")  
    def click_scooter_logo(self):
        logo = self.wait.until(EC.visibility_of_element_located(HomePageLocators.SCOOTER_LOGO))
        self.execute_script_click(logo)  # Используем метод из BasePage

    @allure.step("Переключение на новое окно")  
    def switch_to_new_window(self):
        self.switch_to_window(self.get_window_handles()[-1])  # Используем методы BasePage
        return self

    @allure.step("Закрытие текущего окна")  
    def close_current_window(self):
        if len(self.get_window_handles()) > 1:  # Используем метод BasePage
            self.close_window()  # Используем метод BasePage
            self.switch_to_window(self.get_window_handles()[0])

    @allure.step("Ожидание и проверка URL содержит: {expected_url}")  
    def wait_and_verify_url_contains(self, expected_url, timeout=15):
        self.wait.until(EC.url_contains(expected_url), 
                        message=f"Ожидаемый URL не содержит '{expected_url}'. Текущий URL: {self.get_current_url()}")
        assert expected_url in self.get_current_url(), f"URL не содержит '{expected_url}'. Текущий URL: {self.get_current_url()}"

    @allure.step("Ожидание и проверка URL равен: {expected_url}") 
    def wait_and_verify_url_to_be(self, expected_url, timeout=15):
        self.wait.until(EC.url_to_be(expected_url), 
                        message=f"Ожидаемый URL: '{expected_url}', текущий URL: {self.get_current_url()}")
        assert self.get_current_url() == expected_url, f"URL не равен '{expected_url}'. Текущий URL: {self.get_current_url()}"

    @allure.step("Открытие страницы: {url}") 
    def open_page(self, url):
        self.navigate(url)  

    @allure.step("Ожидание загрузки логотипа Самоката") 
    def wait_for_scooter_logo(self, timeout=20):
        logo = self.wait.until(EC.element_to_be_clickable(HomePageLocators.SCOOTER_LOGO), 
                               message="Логотип Самоката не появился на странице")
        assert logo is not None, "Логотип Самоката не появился на странице"

    def wait_for_new_window(self, timeout=10):  
        self.wait.until(self.new_window_is_opened, message="Не дождались открытия нового окна")

    def new_window_is_opened(self, driver):  
        return len(self.get_window_handles()) > 1  # Используем метод BasePage