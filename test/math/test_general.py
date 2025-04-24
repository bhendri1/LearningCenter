from assertpy import assert_that, soft_assertions

from src.math.general import is_even

from src.math.general import is_odd

from src.math.general import is_divisable

EVEN_NUMBERS = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
42, 44, 46, 48, 50]

ODD_NUMBERS = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 
               
        59, 61, 63, 65, 67, 69, 71]

DIVISABLE_NUMBERS = [3, 6, 9, 15, 18, 21, 27, 30, 33, 39, 42, 45]

DIVISIBLE_PAIRS = [(4, 7, False), (12, 5, False), (12, 3, True), (44, 7, False)]

def test_is_even():
    with soft_assertions():
        for i in range(len(EVEN_NUMBERS)):
            test_num = EVEN_NUMBERS[i]
            assert_that (is_even(test_num), f'{test_num} is even').is_true()

def test_is_even_alt():
    with soft_assertions():
        for test_num in EVEN_NUMBERS:
            assert_that (is_even(test_num), f'{test_num} is even').is_true()

def test_is_odd():
    with soft_assertions():
        for i in range(len(ODD_NUMBERS)):
            test_num = ODD_NUMBERS[i]
            assert_that (is_odd(test_num), f'{test_num} is odd').is_true()

def test_is_divisor():
    with soft_assertions():
        for i in range(len(DIVISABLE_NUMBERS)):
            test_num = DIVISABLE_NUMBERS[i]
            assert_that (is_divisable(test_num, 3), f'{test_num} is divisable by 3').is_true()

def test_is_divisor_should_be_false():
    with soft_assertions():
        for i in range(len(DIVISABLE_NUMBERS)):
            test_num = DIVISABLE_NUMBERS[i]
            assert_that (is_divisable(test_num, 4), f'{test_num} is divisable by 4').is_false()

def test_is_divisor_using_pairs_of_nums():
    with soft_assertions():
        for pair in DIVISIBLE_PAIRS:
            test_num = pair[0]
            divisor = pair[1]
            divisible = pair[2]
            if divisible:
                assert_that (is_divisable(test_num, divisor), f'{test_num} should be divisable by {divisor}').is_true()
            else:
                assert_that (is_divisable(test_num, divisor), f'{test_num} should not be divisable by {divisor}').is_false()

def test_is_divisor_using_pairs_of_nums():
    with soft_assertions():
        for pair in DIVISIBLE_PAIRS:
            test_num, divisor, divisible = pair
            if divisible:
                assert_that (is_divisable(test_num, divisor), f'{test_num} should be divisable by {divisor}').is_true()
            else:
                assert_that (is_divisable(test_num, divisor), f'{test_num} should not be divisable by {divisor}').is_false()

def test_is_divisor_using_pairs_of_nums2():
    with soft_assertions():
        for pair in DIVISIBLE_PAIRS:
            n, d, divisible = pair
            if divisible:
                assert_that (is_divisable(test_num = n, divisor = d), f'{n} should be divisable by {d}').is_true()
            else:
                assert_that (is_divisable(divisor = d, test_num = n), f'{n} should not be divisable by {d}').is_false()

def test_is_divisor_using_pairs_of_nums3():
    with soft_assertions():
        for pair in DIVISIBLE_PAIRS:
            n, d, divisible = pair
            kwargs = {
                "test_num": n, "divisor": d
            }
            if divisible:
                assert_that (is_divisable(**kwargs), f'{n} should be divisable by {d}').is_true()
            else:
                assert_that (is_divisable(**kwargs), f'{n} should not be divisable by {d}').is_false()


