import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 

    @allure.step("Переход по URL: {url}")
    def navigate(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator):  
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except TimeoutException as e:
            print(f"Элемент не кликабельный: {locator}. Ошибка: {e}")
            raise

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def enter_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException as e:
            print(f"Поле ввода не найдено: {locator}. Ошибка: {e}")
            raise

    @allure.step("Проверка наличия элемента: {locator}")
    def element_is_present(self, locator, timeout=10):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False