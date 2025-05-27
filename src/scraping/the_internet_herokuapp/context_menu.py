import selenium
import selenium.common
import selenium.webdriver
import selenium.webdriver.common
from .base import HerokuAPPTestingBase
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys

class ContextMenuPage(HerokuAPPTestingBase):
    def loadPage(self):
        
        ''' 
            Load the 'Context Menu' excercise
            Starting from the 'the-internet.herokuapp' sample site
            find and navigate to the link with text 'Context Menu' 
        '''
        if not self.basePageLoaded:
            self.loadBasePage()
        # find and navigate to the link with text 'Add/Remove Elements'
        self.driver.find_element(By.LINK_TEXT, 'Context Menu').click()
        
    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#hot-spot'))
            )
        except TimeoutError as e:
            print(e, file=sys.stderr)
            raise e
        
    def open_context_menu(self):
        hotSpotDiv = self.driver.find_element(By.CSS_SELECTOR, 'div#hot-spot')
        actions = ActionChains(self.driver)
        actions.context_click(hotSpotDiv).perform()
        
    def is_alert_pop_up_visible(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(EC.alert_is_present(), 'alert is present') != None
        except selenium.common.exceptions.TimeoutException:
            return False
        
    def get_alert_pop_up_message(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(EC.alert_is_present(), 'alert message').text
        except selenium.common.exceptions.TimeoutException:
            return None
        
    def close_alert_pop_up(self):
        WebDriverWait(self.driver, timeout=5).until(EC.alert_is_present(), 'closing alert').dismiss()