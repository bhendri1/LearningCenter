from assertpy import assert_that, soft_assertions

from src.list.basic_list_utils import arange, calc_frequencies, calc_frequencies2, combine, grocery_list, is_ordered, list_of_ones, max_int_value_of_dict, ordered_by_frequencies_then_alpha, preferred_option, remove_values, remove_values_in_place, set_words_by_frequecies, top_N_entries, words_from_text


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
        
        assert_that(grocery_list()).contains('apples')
        assert_that(grocery_list()).contains('juice')

def test_preferred_option_for_oranges_is_mandarin():
    with soft_assertions():
        assert_that(preferred_option('oranges'), 'oranges').is_equal_to('dole')

def test_words_from_text():
    text1 = "The cat sat on the wall"

    assert_that(words_from_text(text1)).is_equal_to(['the', 'cat', 'sat', 'on', 'the', 'wall'])

def test_calc_frequencies():
    assert_that(calc_frequencies(['the', 'cat', 'sat', 'on', 'the', 'wall'])).is_equal_to(
        {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'wall': 1}
    )

def test_calc_frequencies2():
    assert_that(calc_frequencies2(['the', 'cat', 'sat', 'on', 'the', 'wall'])).is_equal_to(
        {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'wall': 1}
    )

def test_max_int_value_of_dict():
    frequency_dict_1 = {
        'word1': 7,
        'word2': 9,
        'word3': 1,
    }
    assert_that(max_int_value_of_dict(frequency_dict_1)).is_equal_to(9)

def test_set_words_by_frequecies():
    words = ['word1','word2', 'word3', 'word4', 'word5', 'word6']
    frequency_dict_1 = {
        'word1': 7,
        'word2': 9,
        'word3': 1,
        'word4': 7,
        'word5': 7,
        'word6': 9,
    }
    with soft_assertions():
        assert_that(set_words_by_frequecies(words, frequency_dict_1, 9), '2 words matched to frequency 9').is_equal_to({'word2', 'word6'})
        assert_that(set_words_by_frequecies(words, frequency_dict_1, 8), 'no matches for frequency 8, but does not return None').is_not_equal_to(None)
        assert_that(set_words_by_frequecies(words, frequency_dict_1, 7), '3 words matched to frequency 7').is_equal_to({'word1', 'word4', 'word5'})
        assert_that(set_words_by_frequecies(words, frequency_dict_1, 6), 'nothing matched to frequency 6, returns an empty set').is_equal_to(set())
        assert_that(set_words_by_frequecies(words, frequency_dict_1, 5), 'nothing matched to frequency 5, but not return an empty dict literal').is_not_equal_to({})
        assert_that(set_words_by_frequecies(words, frequency_dict_1, 4), 'nothing matched to frequency 4, but not return an empty list').is_not_equal_to([])
        assert_that(set_words_by_frequecies(words, frequency_dict_1, 1), 'matched to frequency 1').is_equal_to({'word3'})

def test_top_N_entries():
    text1 = 'How how now brown brown brown cow now'
    assert_that(top_N_entries(text1, 4)).is_equal_to(
        {
            3: 'brown',
            2: ['how', 'now', ],
            1: 'cow'
        }
    )

def test_ordered_by_frequencies_then_alpha():
    freq_dict_1 = {'Bob': 1, 'Fred': 20, 'George': 13, 'Alice': 1}
    with soft_assertions():
        assert_that(ordered_by_frequencies_then_alpha(freq_dict_1)).is_equal_to(['Fred', 'George', 'Alice', 'Bob'])

def test_remove_values():
    num_list = [4, 2, 3, 2, 3 , 1, 7]
    with soft_assertions():
        assert_that(remove_values(num_list, 3)).is_equal_to([4, 2, 2, 1, 7])

def test_remove_values_in_place():
    num_list = [4, 2, 3, 2, 3 , 1, 7]
    with soft_assertions():
        assert_that(num_list, 'original').is_equal_to([4, 2, 3, 2, 3 , 1, 7])
        remove_values_in_place(num_list, 3)
        assert_that(num_list, 'after').is_equal_to([4, 2, 2, 1, 7])