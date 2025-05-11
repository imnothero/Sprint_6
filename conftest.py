import pytest
from selenium import webdriver
import config

@pytest.fixture(scope="function") # фикстура для запуска драйвера на каждый тест отдельно
def driver():
    driver = webdriver.Firefox() 
    driver.get(config.SCOOTER_URL) 
    yield driver    
    driver.quit()
