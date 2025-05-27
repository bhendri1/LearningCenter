from .base import HerokuAPPTestingBase
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys

class DropdownPage(HerokuAPPTestingBase):
    def loadPage(self):
        
        ''' 
            Load the 'Context Menu' excercise
            Starting from the 'the-internet.herokuapp' sample site
            find and navigate to the link with text 'Context Menu' 
        '''
        if not self.basePageLoaded:
            self.loadBasePage()
        # find and navigate to the link with text 'Add/Remove Elements'
        self.driver.find_element(By.LINK_TEXT, 'Dropdown').click()
        
    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'select#dropdown'))
            )
        except TimeoutError as e:
            print(e, file=sys.stderr)
            raise e
        
    def  select_dropdown_item_by_visible_text(self, text):
        dropdownMenu = self.driver.find_element(By.CSS_SELECTOR, 'select#dropdown')
        dropdownMenuSelect = Select(dropdownMenu)
        dropdownMenuSelect.select_by_visible_text(text)
        
        