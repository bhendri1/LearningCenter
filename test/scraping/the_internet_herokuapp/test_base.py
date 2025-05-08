import time
from assertpy import assert_that, soft_assertions

from src.scraping.the_internet_herokuapp.base import HerokuAPPTestingBase

def test_load_base_page():
    testing = HerokuAPPTestingBase()
    testing.loadBasePage()
    time.sleep(5)
    assert_that(testing.isBasePageLoaded()).is_true()
    testing.close()