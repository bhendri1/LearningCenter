import selenium.common
import selenium.webdriver
import selenium.webdriver.common
from .base import HerokuAPPTestingBase
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sys


class DragAndDropPage(HerokuAPPTestingBase):
    def loadPage(self):
        
        ''' 
            Load the 'Context Menu' excercise
            Starting from the 'the-internet.herokuapp' sample site
            find and navigate to the link with text 'Context Menu' 
        '''
        if not self.basePageLoaded:
            self.loadBasePage()
        # find and navigate to the link with text 'Add/Remove Elements'
        self.driver.find_element(By.LINK_TEXT, 'Drag and Drop').click()
        
    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#column-a.column'))
            )
        except TimeoutError as e:
            print(e, file=sys.stderr)
            raise e
        
    def get_header_text_from_column(self, col_name: str) -> str:
        column_div = self.driver.find_element(By.CSS_SELECTOR, f'div#column-{col_name}.column')
        header_elem = column_div.find_element(By.CSS_SELECTOR, 'header')
        return header_elem.text
    
    def perform_drag_drop(self, col_1_name: str, col_2_name: str) -> None:
        draggable = self.driver.find_element(By.CSS_SELECTOR, f'div#column-{col_1_name}.column')
        droppable = self.driver.find_element(By.CSS_SELECTOR, f'div#column-{col_2_name}.column')
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()