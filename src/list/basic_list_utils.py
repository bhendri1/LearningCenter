def list_of_ones(num_elements: int) -> list:
    return [1] * num_elements

def arange(num_elements, start_value = 0) -> list:
    # return list(range(start_value, num_elements + start_value))
    return [start_value + i for i in range(num_elements)]

def combine(list_1: list, list_2: list) -> list:
    return list_1 + list_2

def is_ordered(test_list: list) -> bool:
    return test_list == sorted(test_list) or test_list == sorted(test_list, reverse=True)

def grocery_list():
    return ('apples', 'oranges', 'juice', 'milk')



