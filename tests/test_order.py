import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from config import SCOOTER_URL, YANDEX_DZEN_URL
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from data.data import ORDER_DATA 

@allure.title("Проверка оформления заказа самоката с использованием верхней кнопки")
@allure.description("Проверяет, что при нажатии на верхнюю кнопку 'Заказать' происходит успешное оформление заказа")
def test_order_flow_top_button(driver: WebDriver):
    with allure.step("Инициализация страницы заказа"):
        page = OrderPage(driver)
    with allure.step("Открытие страницы Самоката"):
        page.navigate(SCOOTER_URL)
    with allure.step("Клик на верхнюю кнопку 'Заказать'"):
        page.open_order_page_from_top(ORDER_DATA[0]["personal_data"], ORDER_DATA[0]["rental_data"])
    with allure.step("Проверка сообщения об успешном заказе"):
        assert page.is_success_displayed(), "Сообщение об успешном заказе не появилось."
        success_message = page.get_success_message()
        assert "Заказ оформлен" in success_message, f"Ожидалось сообщение 'Заказ оформлен', получено: {success_message}"

@allure.title("Проверка оформления заказа самоката с использованием нижней кнопки")
@allure.description("Проверяет, что при нажатии на нижнюю кнопку 'Заказать' происходит успешное оформление заказа")
def test_order_flow_bottom_button(driver: WebDriver):
    with allure.step("Инициализация страницы заказа"):
        page = OrderPage(driver)
    with allure.step("Открытие страницы Самоката"):
        page.navigate(SCOOTER_URL)
    with allure.step("Клик на нижнюю кнопку 'Заказать'"):
        page.open_order_page_from_bottom(ORDER_DATA[1]["personal_data"], ORDER_DATA[1]["rental_data"])
    with allure.step("Проверка сообщения об успешном заказе"):
        assert page.is_success_displayed(), "Сообщение об успешном заказе не появилось."
        success_message = page.get_success_message()
        assert "Заказ оформлен" in success_message, f"Ожидалось сообщение 'Заказ оформлен', получено: {success_message}"