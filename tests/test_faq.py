import pytest
from pages.faq_page import FaqPage
from locators.faq_locators import FaqLocators
import allure
from data.constants import FAQ_ANSWERS

@allure.feature("Раздел FAQ")
class TestFaq:
    @pytest.mark.parametrize("question_index", range(len(FAQ_ANSWERS)), ids=[f"Вопрос {i}" for i in range(len(FAQ_ANSWERS))])
    @allure.story("Проверка ответов на вопросы")
    @allure.title("Проверка ответа на вопрос {question_index}")
    @allure.description("Проверяем соответствие фактического ответа ожидаемому")
    def test_faq_answers(self, driver, question_index):
        with allure.step("Инициализация страницы FAQ"):
            faq_page = FaqPage(driver)
        with allure.step(f"Клик на вопрос {question_index}"):
            question_locator = getattr(FaqLocators, f"QUESTION_{question_index}")
            faq_page.click_question(question_locator)
        with allure.step(f"Получение фактического ответа для вопроса {question_index}"):
            answer_locator = getattr(FaqLocators, f"ANSWER_{question_index}")
            actual_answer = faq_page.get_answer_text(answer_locator)
        with allure.step(f"Сравнение фактического и ожидаемого результатов для вопроса {question_index}"):
            expected_answer = FAQ_ANSWERS[question_index]
            assert actual_answer == expected_answer, f"Текст ответа отличается от ожидаемого. Ожидалось: '{expected_answer}', получено: '{actual_answer}'"