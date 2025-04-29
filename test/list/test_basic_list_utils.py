from assertpy import assert_that, soft_assertions

from src.list.basic_list_utils import arange, combine, grocery_list, is_ordered, list_of_ones


def test_list_of_ones():
    with soft_assertions():
        assert_that(list_of_ones(5), 'should be a list with five ones').is_equal_to([1, 1, 1, 1, 1])
        assert_that(list_of_ones(7), 'should be a list with seven ones').is_equal_to([1, 1, 1, 1, 1, 1, 1])

def test_arange():
    with soft_assertions():
        assert_that(arange(5), 'should include range of 5' ).is_equal_to([0,1,2,3,4])
        assert_that(arange(7), 'should include range of 7' ).is_equal_to([0,1,2,3,4,5,6])
        assert_that(arange(5, 2), 'should include range of 7' ).is_equal_to([2,3,4,5,6])

def  test_combine():
    with soft_assertions():
        assert_that(combine([0, 1, 2], [3, 4]), 'combining list1 with list2' ).is_equal_to([0,1,2,3,4])

def test_is_ordered():
    with soft_assertions():
        test_list = [3,2,1,0]
        assert_that(is_ordered(test_list), f'{test_list} should be ordered' ).is_true()
        test_list = [0,1,2,3]
        assert_that(is_ordered(test_list), f'{test_list} should be ordered' ).is_true()
        test_list = [3,1,2,0]
        assert_that(is_ordered(test_list), f'{test_list} should not be ordered' ).is_false()

def test_grocery_list_contains_oranges():
    with soft_assertions():
        assert_that(grocery_list()).contains('oranges')

def test_grocery_list_contains_apples_and_juice():
    with soft_assertions():
        grocery_store = ['Giant', 'Target', 'Wegmans', 'Safeway' ]
        assert_that(grocery_list()).contains('apples')
        assert_that(grocery_list()).contains('juice')