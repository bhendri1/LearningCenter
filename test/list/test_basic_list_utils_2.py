from assertpy import assert_that, fail, soft_assertions, soft_fail

from src.list.basic_list_utils_2 import count_identical_neighbors, count_identical_sets_of_neighbors, dot_product, includes_value, num_occurances, search, search_from_end, search_from_end_2, search_from_end_3, search_from_end_4


def test_dot_product():
    num_list_1 = [1.0, 2.0, 3.0]
    num_list_2 = [1,   2,   3,  4, 5]
    res =        [1.0, 4.0, 9.0, 4, 5]
    with soft_assertions():
        assert_that(dot_product(num_list_1, num_list_2)).is_equal_to(res)
        
def test_dot_product_produces_correct_element_types():
    num_list_1 = [1.0, 2.0, 3.0, 1]
    num_list_2 = [1,   2,   3,   4, 5]
    res =  dot_product(num_list_1, num_list_2)
    
    with soft_assertions():
        assert_that(type(res[0])).is_equal_to(float)
        assert_that(type(res[1])).is_equal_to(float)
        assert_that(type(res[2])).is_equal_to(float)
        assert_that(type(res[3])).is_equal_to(int)
        assert_that(type(res[4])).is_equal_to(int)
    
def test_search():
    test_list_1 = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', ]
    search_val_1 = 'one'
    search_val_2 = 'nine'
    search_val_3 = 'three'
    with soft_assertions():
        assert_that(search(test_list_1, search_val_1), f"expect search({test_list_1}, '{search_val_1}') to equal 0") \
            .is_equal_to(0)
        assert_that(search(test_list_1, search_val_2), f"expect search({test_list_1}, '{search_val_2}') to equal 0") \
            .is_equal_to(-1)
        assert_that(search(test_list_1, search_val_3), f"expect search({test_list_1}, '{search_val_3}') to equal 0") \
            .is_equal_to(2)
    
def test_search_from_end():
    test_list_1 = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', ]
    search_val_1 = 'one'
    search_val_2 = 'nine'
    search_val_3 = 'three'
    with soft_assertions():
        assert_that(search_from_end(test_list_1, search_val_1), f"expect search_from_end({test_list_1}, '{search_val_1}') to equal 0") \
            .is_equal_to(6)
        assert_that(search_from_end(test_list_1, search_val_2), f"expect search_from_end({test_list_1}, '{search_val_2}') to equal 0") \
            .is_equal_to(-1)
        assert_that(search_from_end(test_list_1, search_val_3), f"expect search_from_end({test_list_1}, '{search_val_3}') to equal 0") \
            .is_equal_to(8)
    
def test_search_from_end_2():
    test_list_1 = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', ]
    search_val_1 = 'one'
    search_val_2 = 'nine'
    search_val_3 = 'three'
    with soft_assertions():
        assert_that(search_from_end_2(test_list_1, search_val_1), f"expect search_from_end_2({test_list_1}, '{search_val_1}') to equal 0") \
            .is_equal_to(6)
        assert_that(search_from_end_2(test_list_1, search_val_2), f"expect search_from_end_2({test_list_1}, '{search_val_2}') to equal 0") \
            .is_equal_to(-1)
        assert_that(search_from_end_2(test_list_1, search_val_3), f"expect search_from_end_2({test_list_1}, '{search_val_3}') to equal 0") \
            .is_equal_to(8)
    
def test_search_from_end_3():
    test_list_1 = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', ]
    search_val_1 = 'one'
    search_val_2 = 'nine'
    search_val_3 = 'three'
    with soft_assertions():
        assert_that(search_from_end_3(test_list_1, search_val_1), f"expect search_from_end_3({test_list_1}, '{search_val_1}') to equal 0") \
            .is_equal_to(6)
        assert_that(search_from_end_3(test_list_1, search_val_2), f"expect search_from_end_3({test_list_1}, '{search_val_2}') to equal 0") \
            .is_equal_to(-1)
        assert_that(search_from_end_3(test_list_1, search_val_3), f"expect search_from_end_3({test_list_1}, '{search_val_3}') to equal 0") \
            .is_equal_to(8)
    
def test_search_from_end_4():
    test_list_1 = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', ]
    search_val_1 = 'one'
    search_val_2 = 'nine'
    search_val_3 = 'three'
    with soft_assertions():
        assert_that(search_from_end_4(test_list_1, search_val_1), f"expect search_from_end_4({test_list_1}, '{search_val_1}') to equal 0") \
            .is_equal_to(6)
        assert_that(search_from_end_4(test_list_1, search_val_2), f"expect search_from_end_4({test_list_1}, '{search_val_2}') to equal 0") \
            .is_equal_to(-1)
        assert_that(search_from_end_4(test_list_1, search_val_3), f"expect search_from_end_4({test_list_1}, '{search_val_3}') to equal 0") \
            .is_equal_to(8)
        
def test_includes_value():
    test_list_1 = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'four']
    search_val_1 = 'one'
    search_val_2 = 'nine'
    search_val_3 = 'three'
    search_val_4 = 'four'
    with soft_assertions():
        assert_that(includes_value(test_list_1, search_val_1), f"includes_value({test_list_1}, '{search_val_1}')").is_true()
        assert_that(includes_value(test_list_1, search_val_2), f"includes_value({test_list_1}, '{search_val_2}')").is_false()
        assert_that(includes_value(test_list_1, search_val_3), f"includes_value({test_list_1}, '{search_val_3}')").is_true()
        assert_that(includes_value(test_list_1, search_val_4), f"includes_value({test_list_1}, '{search_val_4}')").is_true()
        
def test_includes_value_2():
    test_list_1 = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'four']
    search_vals =  [('zero', False), ('one', True), ('two', True), ('three', True), ('four', True), ('five', False)]
    with soft_assertions():
        for value_pair in search_vals:
            if value_pair[1]:
                assert_that(includes_value(test_list_1, value_pair[0]), f"includes_value({test_list_1}, '{value_pair[0]}')").is_true()
            else:
                assert_that(includes_value(test_list_1, value_pair[0]), f"includes_value({test_list_1}, '{value_pair[0]}')").is_false()

def test_num_occurances():
    test_list_1 = ['one', 'two', 'three', 'four',  'two', 'three', 'four', 'three', 'four', 'four']
    search_vals = ['zero', 'one', 'two', 'three', 'four']
    with soft_assertions():
        for i in range(len(search_vals)):
            assert_that(num_occurances(test_list_1, search_vals[i]), f'num_occurances({test_list_1}, {search_vals[i]})').is_equal_to(i)
    
def test_count_identical_neighbors():
    list_of_test_pairs = [
        ([2, 3, 4, 2, 3, 4], 0),
        ([2, 3, 4, 4, 2, 3, 4], 1),
        ([2, 2, 2, 2, 2], 4),
        ([2, 2, 4, 4, 5, 5, 3, 2], 3)
    ]
    with soft_assertions():
        for test_pair in list_of_test_pairs:
            test_list = test_pair[0]
            test_expected_result = test_pair[1]
            assert_that(count_identical_neighbors(test_list), f'count_identical_neighbors({test_list})').is_equal_to(test_expected_result)
    
def test_count_identical_sets_of_neighbors():
    '''
            count_identical_neighbors(2, [2, 3, 4, 2, 3, 4]) = 0
            count_identical_neighbors(2, [2, 3, 4, 4, 2, 3, 4]) = 1
            count_identical_neighbors(1, [2, 2, 2, 2, 2]) -> Errror
            count_identical_neighbors(2, [2, 2, 2, 2, 2]) = 4
            count_identical_neighbors(3, [2, 2, 2, 2, 2]) = 3
            count_identical_neighbors(4, [2, 2, 2, 2, 2]) = 2
            count_identical_neighbors(5, [2, 2, 2, 2, 2]) = 1
            count_identical_neighbors(6, [2, 2, 2, 2, 2]) -> Error
    '''
    list_of_no_error_test_params = [
        (2, [2, 3, 4, 2, 3, 4],  0),
        (2, [2, 3, 4, 4, 2, 3, 4], 1),
    ]
    
    list_of_raises_error_test_params = [
        (1, [2, 3, 4, 2, 3, 4]),
        (8, [2, 3, 4, 4, 2, 3, 4]),
    ]
    with soft_assertions():
        for params in list_of_no_error_test_params:
            test_N = params[0]
            test_list = params[1]
            test_expected_result = params[2]
            assert_that(
                count_identical_sets_of_neighbors(test_N, test_list), 
                f'count_identical_sets_of_neighbors({test_N}, {test_list})'
            ).is_equal_to(test_expected_result)
            
        for params in list_of_raises_error_test_params:
            test_N = params[0]
            test_list = params[1]
            try:
                count_identical_sets_of_neighbors(test_N, test_list)
                soft_fail(f'count_identical_sets_of_neighbors({test_N}, {test_list})')
            except Exception as e:
                assert_that(e, f'Exception type is Exception').is_type_of(AssertionError)