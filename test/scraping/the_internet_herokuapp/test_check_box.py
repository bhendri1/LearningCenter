from assertpy import assert_that, soft_assertions

from src.scraping.the_internet_herokuapp.check_box import ManipulateCheckBox

def load_test_page():
    test_page = ManipulateCheckBox()
    test_page.loadPage()
    test_page.wait_for_page_to_load()
    return test_page

def test_page_loads():
    load_test_page()

def test_page_loads_with_two_checkboxes_on_page():
    test_page = load_test_page()
    assert_that(test_page.num_checkboxes()).is_equal_to(2)

def test_page_loads_with_only_one_checked_checkbox():
    test_page = load_test_page()
    assert_that(test_page.num_checked_checkboxes()).is_equal_to(1)

def test_check_first_checkbox():
    with soft_assertions():
        test_page = load_test_page()
        assert_that(test_page.is_checked_checkbox(0)).is_false()
        test_page.click_checkbox(0)
        assert_that(test_page.is_checked_checkbox(0)).is_true()

def test_check_second_checkbox():
    with soft_assertions():
        test_page = load_test_page()
        assert_that(test_page.is_checked_checkbox(1)).is_true()
        test_page.click_checkbox(1)
        assert_that(test_page.is_checked_checkbox(1)).is_false()
        