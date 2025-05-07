import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import SCOOTER_URL
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators

@allure.title("Проверка редиректа на Яндекс по клику на логотип")
@allure.description("Проверяет, что при клике на логотип Яндекса происходит переход на страницу Яндекс.Дзен")
def test_yandex_logo_redirect(driver: WebDriver):
    with allure.step("Инициализация главной страницы"):
        main_page = HomePage(driver)
    with allure.step("Клик на логотип Яндекса"):
        main_page.click_yandex_logo()
    with allure.step("Переключение на новое окно"):
        main_page.switch_to_new_window()
    with allure.step("Проверка URL после редиректа"):
        main_page.wait_and_verify_url_contains('dzen.ru')
    with allure.step("Закрытие текущего окна"):
        main_page.close_current_window()

@allure.title("Проверка редиректа на главную страницу Самоката по клику на логотип")
@allure.description("Проверяет, что при клике на логотип Самоката на странице заказа происходит переход на главную страницу Самоката")
def test_scooter_logo_redirect(driver: WebDriver):
    with allure.step("Инициализация главной страницы"):
        main_page = HomePage(driver)
    with allure.step("Открытие страницы заказа"):
        main_page.open_page(SCOOTER_URL + "/order")
    with allure.step("Ожидание загрузки логотипа Самоката"):
        main_page.wait_for_scooter_logo()
    with allure.step("Клик на логотип Самоката"):
        main_page.click_scooter_logo()
    with allure.step("Проверка URL после редиректа"):
        main_page.wait_and_verify_url_contains("qa-scooter.praktikum-services.ru")