from assertpy import assert_that, soft_assertions

from src.math.prime_utils import is_prime, next_prime

PRIME_NUMBERS = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
]

NOT_PRIME_NUMBERS = [
    0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 
    22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39,
    40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63
]

def test_is_prime():
    with soft_assertions():
        assert_that(is_prime(3), '3 is prime').is_true()
        assert_that(is_prime(4), '4 is not prime').is_false()
        assert_that(is_prime(5), '5 is prime').is_true()
        assert_that(is_prime(6), '6 is not prime').is_false()
        assert_that(is_prime(7), '7 is prime').is_true()
        assert_that(is_prime(8), '8 is not prime').is_false()

def test_is_prime_from_list_of_primes():
    with soft_assertions():
        # looping over the list of prime numbers, by index i
        for i in range(len(PRIME_NUMBERS)):
            # assigning the prime value at index i to the variable test_num
            test_num = PRIME_NUMBERS[i]
            # asserting that the is_prime function returns true for the prime number in test_num
            assert_that(is_prime(test_num), f'{test_num} is prime').is_true()

def test_is_prime_from_list_of_not_primes():
    with soft_assertions():
        for i in range(len(NOT_PRIME_NUMBERS)):
            test_num = NOT_PRIME_NUMBERS[i]
            assert_that(is_prime(test_num), f'{test_num} is prime').is_false()

def test_next_prime():
    next_prime_number = 0
    with soft_assertions():
        next_prime_number = next_prime(next_prime_number)
        assert_that(next_prime_number, 'next prime (1 times) should equal 2').is_equal_to(2)
        next_prime_number = next_prime(next_prime_number)
        assert_that(next_prime_number, 'next prime (2 times) should equal 3').is_equal_to(3)
        next_prime_number = next_prime(next_prime_number)
        assert_that(next_prime_number, 'next prime (3 times) should equal 5').is_equal_to(5)
        
       
def test_next_prime_from_list_of_primes():

    next_prime_number = 0
    with soft_assertions():
        for i in range(len(PRIME_NUMBERS)):
            next_prime_number = next_prime(next_prime_number)
            assert_that(next_prime_number, f'next prime ({i} times) should equal 2').is_equal_to(PRIME_NUMBERS[i])


        
