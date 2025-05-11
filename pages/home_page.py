import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на логотип Яндекса")  
    def click_yandex_logo(self):
        self.click_element(HomePageLocators.YANDEX_LOGO)  
        self.wait_for_new_window()  

    @allure.step("Клик на логотип Самоката")  
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.SCOOTER_LOGO)

    @allure.step("Переключение на новое окно")  
    def switch_to_new_window(self):
        self.switch_to_window(self.get_window_handles()[-1])
        return self

    @allure.step("Закрытие текущего окна")  
    def close_current_window(self):
        if len(self.get_window_handles()) > 1:
            self.close_window()
            self.switch_to_window(self.get_window_handles()[0])

    @allure.step("Ожидание и проверка URL содержит: {expected_url}")  
    def wait_and_verify_url_contains(self, expected_url, timeout=15):
        self.wait_for_url_contains(expected_url, timeout)
        assert expected_url in self.get_current_url(), f"URL не содержит '{expected_url}'. Текущий URL: {self.get_current_url()}"

    @allure.step("Ожидание и проверка URL равен: {expected_url}") 
    def wait_and_verify_url_to_be(self, expected_url, timeout=15):
        self.wait_for_url_to_be(expected_url, timeout)
        assert self.get_current_url() == expected_url, f"URL не равен '{expected_url}'. Текущий URL: {self.get_current_url()}"

    @allure.step("Открытие страницы: {url}") 
    def open_page(self, url):
        self.navigate(url)

    @allure.step("Ожидание загрузки логотипа Самоката") 
    def wait_for_scooter_logo(self, timeout=20):
        self.find_element(HomePageLocators.SCOOTER_LOGO)
        assert self.find_element(HomePageLocators.SCOOTER_LOGO) is not None, "Логотип Самоката не появился на странице"

    def new_window_is_opened(self):  
        return len(self.get_window_handles()) > 1