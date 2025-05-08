import time
from assertpy import assert_that, soft_assertions

from src.scraping.the_internet_herokuapp.add_remove_element import AddRemoveElementPage

def test_page_loads():
    with soft_assertions():
        test_page = AddRemoveElementPage()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        test_page.close()

def test_page_loads_with_zero_elements():
    with soft_assertions():
        test_page = AddRemoveElementPage()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        assert_that(test_page.countElements()).is_zero()
        test_page.close()

def test_add_elements():
    with soft_assertions():
        test_page = AddRemoveElementPage()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        assert_that(test_page.countElements(), 'number of elements is empty on load').is_zero()
        test_page.addElement()
        assert_that(test_page.countElements(), 'number of elements after add').is_equal_to(1)
        test_page.addElement()
        assert_that(test_page.countElements(), 'number of elements after add').is_equal_to(2)
        test_page.addElement()
        assert_that(test_page.countElements(), 'number of elements after add').is_equal_to(3)
        test_page.addElement()
        assert_that(test_page.countElements(), 'number of elements after add').is_equal_to(4)
        test_page.close()

def test_add_elements_loop():
    with soft_assertions():
        test_page = AddRemoveElementPage()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        assert_that(test_page.countElements(), 'number of elements is empty on load').is_zero()
        for i in range(1, 21):
            test_page.addElement()
            assert_that(test_page.countElements(), f'number of elements after {i} adds').is_equal_to(i)
        test_page.addElement()
        test_page.close()

def test_pop_elements():
    raise NotImplementedError()

def test_pop_front_elements():
    raise NotImplementedError()

def test_pop_nth_elements():
    raise NotImplementedError()