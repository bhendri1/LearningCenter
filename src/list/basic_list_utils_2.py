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

