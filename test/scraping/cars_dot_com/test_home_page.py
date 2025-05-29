import time
from assertpy import assert_that, soft_assertions

from src.scraping.cars_dot_com.page_objects.base_page_object import CarsDotComTestingBase

USED_STATUS = ('Used', 'used')

TESTING_STATUSES = [
    USED_STATUS
]

def test_load_home_page():
    testing = CarsDotComTestingBase()
    testing.loadHomePage()
    assert_that(testing.isHomePageLoaded()).is_true()
    testing.close()
    

def test_set_new_used_filter():
    with soft_assertions():
        testing = CarsDotComTestingBase()
        testing.loadHomePage()
        for status in TESTING_STATUSES:
            status_txt = status[0]
            status_value = status[1]
            testing.home_page.set_new_used_filter_by_text(status_txt)
            assert_that(testing.home_page.get_new_used_filter_text()).is_equal_to(status_txt)
            assert_that(testing.home_page.get_new_used_filter_value()).is_equal_to(status_value)
            time.sleep(5)
    