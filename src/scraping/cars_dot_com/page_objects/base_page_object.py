from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.scraping.cars_dot_com.config.urls import HOME_PAGE_URL
from src.scraping.cars_dot_com.page_objects.home_page import HomePage

class CarsDotComTestingBase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self)
        
    def loadHomePage(self):
        self.driver.get(HOME_PAGE_URL)
        
    def isHomePageLoaded(self) -> bool:
        try:
            # TODO - uncomment and fix
            # WebDriverWait(self.driver, 10).until(
            #     ???
            # )
            return True
        except TimeoutError as e:
            return False
    def close(self):
        self.driver.close()