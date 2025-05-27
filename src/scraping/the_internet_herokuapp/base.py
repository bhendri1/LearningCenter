from selenium import webdriver

class HerokuAPPTestingBase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self._basePageLoaded = False
    
    def loadBasePage(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        if self.driver.current_url == 'https://the-internet.herokuapp.com/':
            self._basePageLoaded = True

    def isBasePageLoaded(self) -> bool:
        return self.driver.current_url == 'https://the-internet.herokuapp.com/'

    def close(self):
        print('closing')
        self.driver.close()

    @property
    def basePageLoaded(self):
        return self._basePageLoaded