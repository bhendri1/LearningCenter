from selenium.webdriver.common.by import By

from .base import HerokuAPPTestingBase

class AddRemoveElementPage(HerokuAPPTestingBase):
    
    def loadPage(self):
        ''' 
            Load the 'Add/Remove Elements' excercise
            Starting from the 'the-internet.herokuapp' sample site
            find and navigate to the link with text 'Add/Remove Elements' 
        '''
        if not self.basePageLoaded:
            self.loadBasePage()
        # find and navigate to the link with text 'Add/Remove Elements'
        self.driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def isPageLoaded(self) -> bool:
        return self.driver.current_url == 'https://the-internet.herokuapp.com/add_remove_elements/'

    def countElements(self):
        '''
            Once on the 'Add/Remove Elements' excercise
            Return the number of elements in the list of elements
        '''
        elementContainerDiv = self.driver.find_element(By.CSS_SELECTOR, 'div#elements' )
        elementCollection = elementContainerDiv.find_elements(By.CSS_SELECTOR, 'button.added-manually')
        return len(elementCollection)

    def addElement(self):
        '''
            Once on the 'Add/Remove Elements' excercise
            Click the add button once to add a new element to the list of elements
        '''
        self.driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()

    def popElement(self):
        '''
            Once on the 'Add/Remove Elements' excercise
            Remove the last element in the list of elements
        '''
        elementList = self.driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
        elementList[-1].click()

    def popFrontElement(self):
        '''
            Once on the 'Add/Remove Elements' excercise
            Remove the first element in the list of elements
        '''
        elementList = self.driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
        elementList[0].click()

    def popNthElement(self, n: int):
        '''
            Once on the 'Add/Remove Elements' excercise
            Remove the nth element in the list of elements
            if there is no nth element raise an IndexError 
        '''
        elementList = self.driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
        elementList[n].click()