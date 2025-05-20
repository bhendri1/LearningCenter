from .base import HerokuAPPTestingBase
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys

class ManipulateCheckBox(HerokuAPPTestingBase):
    def loadPage(self):
        
        ''' 
            Load the 'Broken Images' excercise
            Starting from the 'the-internet.herokuapp' sample site
            find and navigate to the link with text 'Broken Images' 
        '''
        if not self.basePageLoaded:
            self.loadBasePage()
        # find and navigate to the link with text 'Add/Remove Elements'
        self.driver.find_element(By.LINK_TEXT, 'Checkboxes').click()
        
    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'form#checkboxes'))
            )
        except TimeoutError as e:
            print(e, file=sys.stderr)
            raise e
        
    def num_checkboxes(self) -> bool: # on this page there are 2 checkboxes i.e. i = 0 or 1
        checkBoxElems = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        return len(checkBoxElems)
        
    def num_checked_checkboxes(self) -> bool: # on this page there are 2 checkboxes i.e. i = 0 or 1
        checkBoxElems = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]:checked')
        return len(checkBoxElems)
        
    def num_unchecked_checkboxes(self) -> bool: # on this page there are 2 checkboxes i.e. i = 0 or 1
        checkBoxElems = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]:unchecked')
        return len(checkBoxElems)
        
    def num_checked_checkboxes_2(self) -> bool: # on this page there are 2 checkboxes i.e. i = 0 or 1
        checkBoxElems = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        count = 0
        for cb in checkBoxElems:
            if cb.is_selected():
                count += 1
        return count
        
    def num_unchecked_checkboxes_2(self, i: int) -> bool: # on this page there are 2 checkboxes i.e. i = 0 or 1
        checkBoxElems = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        count = 0
        for cb in checkBoxElems:
            if not cb.is_selected():
                count += 1
        return count
        
    def is_checked_checkbox(self, i: int) -> bool: # on this page there are 2 checkboxes i.e. i = 0 or 1
        checkBoxElems = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        return checkBoxElems[i].is_selected()
    
    def click_checkbox(self, i: int) -> None:
        checkBoxElems = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        checkBoxElems[i].click()