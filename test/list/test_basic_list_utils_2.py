from assertpy import assert_that, soft_assertions

from src.list.basic_list_utils_2 import dot_product, includes_value, num_occurances, search, search_from_end, search_from_end_2, search_from_end_3, search_from_end_4


def test_dot_product():
    num_list_1 = [1.0, 2.0, 3.0]
    num_list_2 = [1, 2, 3,  4, 5]
    res =        [1.0, 4.0, 9.0, 4, 5]
    with soft_assertions():
        assert_that(dot_product(num_list_1, num_list_2)).is_equal_to(res)
    
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
        


                    

