from email.mime import image
import time
from selenium.webdriver.common.by import By

from src.scraping.the_internet_herokuapp.base import HerokuAPPTestingBase


def isBrokenImage(image) -> bool:
    if image and int(image.get_attribute("naturalWidth")) > 0:
        return True
    return False

class  DetectBrokenImages(HerokuAPPTestingBase):
    def loadPage(self):
        ''' 
            Load the 'Broken Images' excercise
            Starting from the 'the-internet.herokuapp' sample site
            find and navigate to the link with text 'Broken Images' 
        '''
        if not self.basePageLoaded:
            self.loadBasePage()
        # find and navigate to the link with text 'Add/Remove Elements'
        self.driver.find_element(By.LINK_TEXT, 'Broken Images').click()

    def isPageLoaded(self) -> bool:
        return self.driver.current_url == 'https://the-internet.herokuapp.com/broken_images'
    
    def isBrokenImagesByAltText(self, altText: str) -> bool:
        images = self.driver.find_elements(By.XPATH, f'//img[contains(@alt, "{altText}")]')
        if len(images) == 1:
            return  isBrokenImage(images[0])
        return False
    
    def numBrokenImages(self) -> int:
        images = self.driver.find_elements(By.XPATH, f'//img')
        broken_count = 0
        for img in images:
            if isBrokenImage(img):
                broken_count += 1
        return broken_count
    
    def numUnbrokenImages(self) -> int:
        images = self.driver.find_elements(By.XPATH, f'//img')
        unbroken_count = 0
        for img in images:
            if not isBrokenImage(img):
                unbroken_count += 1
        return unbroken_count