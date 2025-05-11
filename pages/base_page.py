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
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Проверка наличия элемента: {locator}")
    def element_is_present(self, locator, timeout=10):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_element_invisibility(self, locator, timeout=10):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Клик по элементу через JavaScript: {element}")
    def execute_script_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Переключение на окно: {window_handle}")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Получение списка окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Закрытие текущего окна")
    def close_window(self):
        self.driver.close()

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание URL содержит: {expected_url}")
    def wait_for_url_contains(self, expected_url, timeout=15):
        self.wait.until(EC.url_contains(expected_url))

    @allure.step("Ожидание URL равен: {expected_url}")
    def wait_for_url_to_be(self, expected_url, timeout=15):
        self.wait.until(EC.url_to_be(expected_url))

    @allure.step("Ожидание открытия нового окна")
    def wait_for_new_window(self, timeout=10):
        self.wait.until(lambda x: len(self.get_window_handles()) > 1)