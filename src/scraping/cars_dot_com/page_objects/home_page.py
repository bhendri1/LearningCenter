from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class HomePage:
    def __init__(self, base):
        self.base = base
        
    def _get_stock_type_select_element(self):
        return self.base.driver.find_element(By.NAME, 'stock_type')
        
    def _select_option_by_text(self, select: WebElement, option_text) -> None:
        option_list = select.find_elements(By.TAG_NAME, 'option')
        for option in option_list:
            if option.text == option_text:
                option.click()
                return
        raise ValueError(f'{option_text} is not a valid option for select {select.get_property("name")}')
        
    def set_new_used_filter_by_text(self, status: str) -> None:
        stock_type_select = self._get_stock_type_select_element()
        self._select_option_by_text(stock_type_select, status)
               
        
    
    def get_new_used_filter_text(self) -> str:
        pass
    
    def get_new_used_filter_value(self) -> str:
        pass