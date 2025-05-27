import time
from assertpy import assert_that, soft_assertions

from src.scraping.the_internet_herokuapp.context_menu import ContextMenuPage

def load_test_page():
    test_page = ContextMenuPage()
    test_page.loadPage()
    test_page.wait_for_page_to_load()
    return test_page

def test_page_loads():
    load_test_page()

def test_open_context_menu():
    with soft_assertions():
        test_page = load_test_page()
        test_page.open_context_menu()
        assert_that(test_page.is_alert_pop_up_visible()).is_true()
        assert_that(test_page.get_alert_pop_up_message()).is_equal_to("You selected a context menu")
        test_page.close_alert_pop_up()
        