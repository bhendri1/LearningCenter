import math


def reverse_order(list_1: list[any]) -> list[any]:
    result_list = []
    '''
        looping in order -> range(len(list_1)) ~ range(0, len(list_1), 1), 
        reverse order -> range(-1, -len(list_1) -1, -1) or rangle(len(list_1) -1, -1, -1)
    '''
    for i in range(len(list_1)):  
        result_list.append(list[i])
    return result_list

def reverse_order_in_place(list: list[any]) -> None:
    pass

def dot_product(num_list_1: list[int|float], num_list_2: list[int|float]) -> list[int|float]:
    '''
        return the dot product of the two lists, will treat the shorter list as though the missing elements were all one.
        the type of the returned value will be an integer if both are ints or a float if one or more values is a float
        ie.
            dot_product([1.0, 2.0, 3.0], [1, 2, 3, 4, 5]) = [1.0, 4.0, 9.0, 4, 5]
    '''
    result_list = []
    len_1 = len(num_list_1)
    len_2 = len(num_list_2)
    min_len = len_1 if len_1 <= len_2 else len_2 # min(len_1, len_2)
    for i in range(min_len):
        result_list.append(num_list_1[i] * num_list_2[i])
    if len_1 > len_2:
        for i in range(min_len, len_1):
            result_list.append(num_list_1[i])
    elif len_2 > len_1:
        for i in range(min_len, len_2):
            result_list.append(num_list_2[i])
    
    return result_list

def dot_product_2(num_list_1: list[int|float], num_list_2: list[int|float]) -> list[int|float]:
    '''
        return the dot product of the two lists, will treat the shorter list as though the missing elements were all one.
        the type of the returned value will be an integer if both are ints or a float if one or more values is a float
        ie.
            dot_product([1.0, 2.0, 3.0], [1, 2, 3, 4, 5]) = [1.0, 4.0, 9.0, 4, 5]
    '''
    result_list = []
    len_1 = len(num_list_1)
    len_2 = len(num_list_2)
    max_len = math.max(len_1, len_2)
    for i in range(max_len):
        num_1 = num_list_1[i] if i < len_1 else 1
        num_2 = num_list_2[i] if i < len_2 else 1
        result_list.append(num_1 * num_2)
    
    return result_list

def search(list_1: list[any], search_val: any) -> int:
    '''
        return the index of the first element in the list which equals the search value, 
        otherwise returns -1 if value is not found
    '''
    for i in range(len(list_1)):
        if list_1[i] == search_val:
            return i
    return -1


def search_from_end(list_1: list[any], search_val: any) -> int:
    '''
        return the index of the last element in the list which equals the search value, 
        other wise returns -1 if value is not found
    '''
    for i in range(len(list_1)):
        j = (len(list_1) - 1) - i
        if list_1[j] == search_val:
            return j
    return -1


def search_from_end_2(list_1: list[any], search_val: any) -> int:
    '''
        return the index of the last element in the list which equals the search value, 
        other wise returns -1 if value is not found
    '''
    for i in range(1, len(list_1) + 1):
        if list_1[-i] == search_val:
            return len(list_1) - i
    return -1

def search_from_end_3(list_1: list[any], search_val: any) -> int:
    '''
        return the index of the last element in the list which equals the search value, 
        other wise returns -1 if value is not found
    '''
    for i in range(-1, -len(list_1), -1):
        if list_1[i] == search_val:
            return len(list_1) + i
    return -1

def search_from_end_4(list_1: list[any], search_val: any) -> int:
    '''
        return the index of the last element in the list which equals the search value, 
        other wise returns -1 if value is not found
    '''
    for i in range(len(list_1) - 1, -1, -1):
        if list_1[i] == search_val:
            return i
    return -1

def search_from_end_4(list_1: list[any], search_val: any) -> int:
    '''
        return the index of the last element in the list which equals the search value, 
        other wise returns -1 if value is not found
    '''
    i = len(list_1) - 1
    while i >= 0:
        if list_1[i] == search_val:
            return i
        i -= 1
    return -1

def includes_value(list_1: list[any], search_val: any) -> bool:
    '''
        returns true if search_val is equal to one or more elements in the list
    '''
    num_elementsinList_1 = len(list_1)
    for i in range(num_elementsinList_1): # 0, 1, 2, ... (num_elementsinList_1 - 1)
        if list_1[i] == search_val:
            return True
    return False

def num_occurances(list_1: list[any], search_value: any) -> int:
    '''
        returns number of occurances of val inside the list
    '''
    count = 0
    for val in list_1:
        if val == search_value:
            count += 1
    return count

def count_identical_neighbors(list_1: list[int]) -> int:
    '''
        count the number of possible pairs of elements in a list, that have the same value, 
        and are next to each other in the list order.
        
        ex:
            count_identical_neighbors([2, 3, 4, 2, 3, 4]) = 0
            count_identical_neighbors([2, 3, 4, 4, 2, 3, 4]) = 1
            count_identical_neighbors([2, 2, 2, 2, 2]) = 4
    '''
    count = 0

    for i in range(len(list_1) - 1):
        val_1 = list_1[i]
        val_2 = list_1[i + 1]
        if val_1 == val_2:
            count += 1
    
    return count

def count_identical_sets_of_neighbors(N: int, list_1: list[int]) -> int:
    '''
        count the number of possible subsets of size N of elements in a list, 
        that have the same value, 
        and are next to each other in the list order.
        
        Raise an error if N is less than 2, or greater than the length of the list
        
        ex:
            count_identical_neighbors(2, [2, 3, 4, 2, 3, 4]) = 0
            count_identical_neighbors(2, [2, 3, 4, 4, 2, 3, 4]) = 1
            count_identical_neighbors(1, [2, 2, 2, 2, 2]) -> Errror
            count_identical_neighbors(2, [2, 2, 2, 2, 2]) = 4
            count_identical_neighbors(3, [2, 2, 2, 2, 2]) = 3
            count_identical_neighbors(4, [2, 2, 2, 2, 2]) = 2
            count_identical_neighbors(5, [2, 2, 2, 2, 2]) = 1
            count_identical_neighbors(6, [2, 2, 2, 2, 2]) -> Error
    '''
    count = 0
        
    #assert N >= 2, f"N must be greater than or equal to 2 ({N} < 2)"
    #assert  N <= len(list_1), f"N cannot be greater than list length {len(list_1)} ({N} > {len(list_1)})"

    for i in range(len(list_1) - N + 1):
        identical = True
        for j in range(1, N): # Why N minus 1?
            if list_1[i] != list_1[i + j]:
                identical = False
                break
        if identical:
            count += 1
    
    return count