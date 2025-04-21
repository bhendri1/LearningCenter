from assertpy import assert_that, soft_assertions

from src.math.prime_utils import is_prime

def test_is_prime_function():
    with soft_assertions():
        assert_that(is_prime(3), '3 is prime').is_true()
        assert_that(is_prime(4), '4 is not prime').is_false()
        assert_that(is_prime(5), '5 is prime').is_true()
        assert_that(is_prime(6), '6 is not prime').is_false()
        assert_that(is_prime(7), '7 is prime').is_true()