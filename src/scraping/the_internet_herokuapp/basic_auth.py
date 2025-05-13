import time
from selenium.webdriver.common.by import By

from src.scraping.the_internet_herokuapp.base import HerokuAPPTestingBase

class BasicAuthPage(HerokuAPPTestingBase):  
    def loadPage(self, username, password):
        ''' 
            Load the 'Basic Auth' excercise
            Starting from the 'the-internet.herokuapp' sample site
            find and navigate to the link with text 'Basic Auth (user and pass: admin)' 
        '''
        if not self.basePageLoaded:
            self.loadBasePage()
        # find and navigate to the link with text 'Add/Remove Elements'
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, 'Basic Auth').click()
        time.sleep(5)