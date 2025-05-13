import time
from assertpy import assert_that, soft_assertions

from src.scraping.the_internet_herokuapp.broken_images import DetectBrokenImages

def test_page_loads():
    with soft_assertions():
        test_page = DetectBrokenImages()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        test_page.close()

def test_page_contains_unbroken_image_by_alt_text():
    with soft_assertions():
        test_page = DetectBrokenImages()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        assert_that(test_page.isBrokenImagesByAltText('Fork me on GitHub')).is_true()
        test_page.close()

def test_page_contains_two_broken_images():
    with soft_assertions():
        test_page = DetectBrokenImages()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        assert_that(test_page.numBrokenImages()).is_equal_to(2)
        test_page.close()

def test_page_contains_two_unbroken_images():
    with soft_assertions():
        test_page = DetectBrokenImages()
        test_page.loadPage()
        assert_that(test_page.isPageLoaded()).is_true()
        assert_that(test_page.numUnbrokenImages()).is_equal_to(2)
        test_page.close()
