from selenium.webdriver.common.by import By


class FaqLocators:  # локаторы для элементов раздела "Вопросы и ответы" на главной странице
    # локаторы для вопросов
    QUESTION_0 = (By.ID, "accordion__heading-0")
    QUESTION_1 = (By.ID, "accordion__heading-1")
    QUESTION_2 = (By.ID, "accordion__heading-2")
    QUESTION_3 = (By.ID, "accordion__heading-3")
    QUESTION_4 = (By.ID, "accordion__heading-4")
    QUESTION_5 = (By.ID, "accordion__heading-5")
    QUESTION_6 = (By.ID, "accordion__heading-6")
    QUESTION_7 = (By.ID, "accordion__heading-7")

    # локаторы для ответов
    ANSWER_0 = (By.ID, "accordion__panel-0")
    ANSWER_1 = (By.ID, "accordion__panel-1")
    ANSWER_2 = (By.ID, "accordion__panel-2")
    ANSWER_3 = (By.ID, "accordion__panel-3")
    ANSWER_4 = (By.ID, "accordion__panel-4")
    ANSWER_5 = (By.ID, "accordion__panel-5")
    ANSWER_6 = (By.ID, "accordion__panel-6")
    ANSWER_7 = (By.ID, "accordion__panel-7")
