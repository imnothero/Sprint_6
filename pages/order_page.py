import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from config import SCOOTER_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class OrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Открытие страницы заказа через кнопку вверху")
    def open_order_page_from_top(self, personal_data, rental_data):
        with allure.step("Переход на страницу заказа"):
            self.navigate(SCOOTER_URL)
        with allure.step("Клик по верхней кнопке 'Заказать'"):
            self.click_order_button(OrderPageLocators.ORDER_BUTTON_TOP)
        with allure.step("Заполнение личной информации"):
            self.fill_personal_info(*personal_data)
        with allure.step("Заполнение информации об аренде"):
            self.fill_rental_info(**rental_data)

    @allure.step("Открытие страницы заказа через кнопку внизу")
    def open_order_page_from_bottom(self, personal_data, rental_data):
        with allure.step("Переход на страницу заказа"):
            self.navigate(SCOOTER_URL)
        with allure.step("Клик по нижней кнопке 'Заказать'"):
            self.click_order_button(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        with allure.step("Заполнение личной информации"):
            self.fill_personal_info(*personal_data)
        with allure.step("Заполнение информации об аренде"):
            self.fill_rental_info(**rental_data)

    @allure.step("Клик на кнопку 'Заказать' с локатором: {button_locator}")
    def click_order_button(self, button_locator):
        with allure.step("Ожидание исчезновения спиннера"):
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(OrderPageLocators.MODAL_OVERLAY)
                )
            except TimeoutException:
                print("Спиннер не исчез вовремя.")
        
        with allure.step("Клик по кнопке"):
            element = self.wait.until(EC.element_to_be_clickable(button_locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()

    @allure.step("Заполнение личной информации")
    def fill_personal_info(self, name, surname, address, metro_station, phone):
        with allure.step(f"Ввод имени: {name}"):
            self.enter_text(OrderPageLocators.FIRST_NAME, name)
        with allure.step(f"Ввод фамилии: {surname}"):
            self.enter_text(OrderPageLocators.SURNAME, surname)
        with allure.step(f"Ввод адреса: {address}"):
            self.enter_text(OrderPageLocators.ADDRESS, address)
        with allure.step(f"Ввод телефона: {phone}"):
            self.enter_text(OrderPageLocators.PHONE, phone)
        with allure.step("Выбор станции метро"):
            self.select_metro_station(metro_station)
        with allure.step("Клик на кнопку 'Далее'"):
            self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбор станции метро: {station_name}")
    def select_metro_station(self, station_name):
        self.click_element(OrderPageLocators.METRO_INPUT)
        metro_station_locator = (By.XPATH, f"//li[@class='select-search__row' and contains(., '{station_name}')]")
        self.click_element(metro_station_locator)
        selected_station = self.find_element(OrderPageLocators.METRO_INPUT)
        assert station_name in selected_station.get_attribute("value"), f"Станция {station_name} не выбрана"

    @allure.step("Заполнение информации об аренде")
    def fill_rental_info(self, date, rental_period, color, comment):
        with allure.step("Выбор даты доставки"):
            self.select_date(date)
        with allure.step("Выбор срока аренды"):
            self.select_rental_period(rental_period)
        with allure.step(f"Выбор цвета самоката: {color}"):
            color_locator = OrderPageLocators.COLOR_BLACK if color.lower() == "black" else OrderPageLocators.COLOR_GREY
            self.click_element(color_locator)
        with allure.step("Ввод комментария для курьера"):
            self.enter_text(OrderPageLocators.COMMENT, comment)
        with allure.step("Клик на кнопку 'Заказать'"):
            self.click_element(OrderPageLocators.ORDER_BUTTON)
        with allure.step("Подтверждение заказа"):
            self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Выбор даты доставки: {date}")
    def select_date(self, date):
        self.click_element(OrderPageLocators.RENTAL_DATE)
        day = date.split(".")[0]  
        date_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{day}']")
        self.click_element(date_locator)

    @allure.step("Выбор срока аренды: {period}")
    def select_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        period_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
        self.click_element(period_locator)

    @allure.step("Проверка отображения сообщения об успешном заказе")
    def is_success_displayed(self):
        return self.element_is_present(OrderPageLocators.SUCCESS_MODAL)

    @allure.step("Получение текста сообщения об успешном заказе")
    def get_success_message(self):
        return self.find_element(OrderPageLocators.SUCCESS_MODAL).text