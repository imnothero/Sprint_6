import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_locators import FaqLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class FaqPage(BasePage):

    def __init__(self, driver: WebDriver):  
        super().__init__(driver)

    @allure.step("Клик на вопрос: {question_locator}")
    def click_question(self, question_locator): 
        max_attempts = 3  
        for attempt in range(max_attempts):
            try:
                with allure.step(f"Попытка {attempt + 1}: Клик на вопрос: {question_locator}"):
                    self.click_element(question_locator)
                    return self
            except (TimeoutException, ElementClickInterceptedException) as e:
                print(f"Попытка {attempt + 1} клика не удалась: {e}")
                if attempt == max_attempts - 1:
                    print(f"Вопрос не кликабельный после {max_attempts} попыток: {question_locator}")
                    raise 
        return self

    @allure.step("Получение текста ответа: {answer_locator}")
    def get_answer_text(self, answer_locator): 
        return self.find_element(answer_locator).text