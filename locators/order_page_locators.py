from selenium.webdriver.common.by import By


class OrderPageLocators:  # Локаторы для элементов страницы оформления заказа
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[contains(text(), 'Заказать')])[1]")  # Верхняя кнопка "Заказать" на странице
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")  # Нижняя кнопка "Заказать" на странице

    # 1. Поля формы "Для кого самокат"
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле для ввода имени
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле для ввода фамилии
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле для ввода адреса доставки
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле для ввода номера телефона

    # Элементы выбора станции метро
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле для ввода станции метро
    METRO_STATION = (By.XPATH, "//li[@class='select-search__row' and contains(., '{}')]")  # Шаблон для выбора станции метро

    # Кнопка перехода к следующему шагу
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")  # Кнопка "Далее" после заполнения формы "Для кого самокат"

    # 2. Поля формы "Про аренду"
    RENTAL_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле для выбора даты доставки
    DATE_PICKER_DAY = (By.XPATH,
                       "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{}']")  # Шаблон для выбора дня в календаре
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")  # Выпадающий список для выбора срока аренды
    PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")  # Выбор опции "сутки" в списке срока аренды
    COLOR_BLACK = (By.ID, "black")  # Чекбокс для выбора чёрного цвета самоката
    COLOR_GREY = (By.ID, "grey")  # Чекбокс для выбора серого цвета самоката
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле для ввода комментария курьеру

    # Кнопки подтверждения заказа
    ORDER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")  # Кнопка "Заказать" на форме "Про аренду"
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")  # Кнопка "Да" в модальном окне подтверждения
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")  # Модальное окно с текстом успешного оформления заказа

    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'spinner')]")  # Локатор для спиннера (индикатор загрузки)ы