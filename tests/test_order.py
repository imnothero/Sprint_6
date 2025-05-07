import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from config import SCOOTER_URL, YANDEX_DZEN_URL
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage

# Наборы данных для тестирования
ORDER_DATA = [
    {
        "personal_data": ("Иван", "Иванов", "Москва, ул. Ленина, 1", "Сокольники", "+79991234567"),
        "rental_data": {
            "date": "15.05.2025",
            "rental_period": "сутки",
            "color": "black",
            "comment": "Оставьте у двери"
        }
    },
    {
        "personal_data": ("Анна", "Петрова", "Москва, ул. Победы, 10", "Тульская", "+79997654321"),
        "rental_data": {
            "date": "16.05.2025",
            "rental_period": "двое суток",
            "color": "grey",
            "comment": "Позвоните за час до доставки"
        }
    }
]

@pytest.mark.parametrize("button_locator, order_data", [
    (OrderPageLocators.ORDER_BUTTON_TOP, ORDER_DATA[0]),
    (OrderPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA[1])
], ids=["top_button", "bottom_button"])
@allure.title("Проверка оформления заказа самоката с использованием кнопки {button_locator}")
@allure.description("Проверяет, что при нажатии на кнопку 'Заказать' (верхнюю или нижнюю) происходит успешное оформление заказа")
def test_order_flow(driver: WebDriver, button_locator, order_data):
    with allure.step("Инициализация страницы заказа"):
        page = OrderPage(driver)
    with allure.step("Открытие страницы Самоката"):
        page.navigate(SCOOTER_URL)
    with allure.step("Клик на кнопку 'Заказать'"):
        if button_locator == OrderPageLocators.ORDER_BUTTON_TOP:
            page.open_order_page_from_top(order_data["personal_data"], order_data["rental_data"])
        else:
            page.open_order_page_from_bottom(order_data["personal_data"], order_data["rental_data"])
    with allure.step("Проверка сообщения об успешном заказе"):
        assert page.is_success_displayed(), "Сообщение об успешном заказе не появилось."
        success_message = page.get_success_message()
        assert "Заказ оформлен" in success_message, f"Ожидалось сообщение 'Заказ оформлен', получено: {success_message}"