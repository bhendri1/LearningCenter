import time
from assertpy import assert_that, soft_assertions

from src.scraping.the_internet_herokuapp.drag_and_drop import DragAndDropPage


def load_test_page():
    test_page = DragAndDropPage()
    test_page.loadPage()
    test_page.wait_for_page_to_load()
    return test_page

def test_page_loads():
    load_test_page()
    
def test_initial_col_setup():
    with soft_assertions():
        test_page = load_test_page()
        assert_that(test_page.get_header_text_from_column('a')).is_equal_to('A')
        assert_that(test_page.get_header_text_from_column('b')).is_equal_to('B')
    
def test_drag_drop():
    with soft_assertions():
        test_page = load_test_page()
        assert_that(test_page.get_header_text_from_column('a')).is_equal_to('A')
        assert_that(test_page.get_header_text_from_column('b')).is_equal_to('B')
        test_page.perform_drag_drop('a', 'b')
        assert_that(test_page.get_header_text_from_column('a')).is_equal_to('B')
        assert_that(test_page.get_header_text_from_column('b')).is_equal_to('A')
        test_page.perform_drag_drop('a', 'b')
        assert_that(test_page.get_header_text_from_column('a')).is_equal_to('A')
        assert_that(test_page.get_header_text_from_column('b')).is_equal_to('B')
        test_page.perform_drag_drop('b', 'a')
        assert_that(test_page.get_header_text_from_column('a')).is_equal_to('B')
        assert_that(test_page.get_header_text_from_column('b')).is_equal_to('A')
        test_page.perform_drag_drop('b', 'a')
        assert_that(test_page.get_header_text_from_column('a')).is_equal_to('A')
        assert_that(test_page.get_header_text_from_column('b')).is_equal_to('B')
