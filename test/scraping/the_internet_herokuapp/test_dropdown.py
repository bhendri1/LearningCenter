import time
from assertpy import assert_that, soft_assertions

from src.scraping.the_internet_herokuapp.dropdown import DropdownPage

def load_test_page():
    test_page = DropdownPage()
    test_page.loadPage()
    test_page.wait_for_page_to_load()
    return test_page

def test_page_loads():
    load_test_page()

def test_select_dropdown_item():
    with soft_assertions():
        test_page = load_test_page()
        test_page.select_dropdown_item_by_visible_text('Option 2')
        time.sleep(5)
        

        