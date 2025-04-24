def prime_generator():
    pass

def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def not_prime(num):
    return not is_prime(num)

def is_prime_2(num):
    if num == 0 or num == 1:
        return False
    
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

def next_prime(num):
    test_num = num + 1
    while not is_prime(test_num):
        test_num += 1
    return test_num

def next_prime_2(num):
    test_num = num + 1
    while is_prime(test_num) == False:
        test_num += 1
    return test_num