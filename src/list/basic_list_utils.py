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

def preferred_option(item: str) -> str:
    match item:
        case 'apples':
            return 'red delicious'
        case 'oranges':
            return 'mandarin'
        case 'juice':
            return 'dole'
        case 'milk':
            return 'whole'
        case default:
            raise KeyError(f'unknown item type: {item}')
    

def preferred_option2(item: str) -> str:
    preferrences = {
        'apples': 'red delicious',
        'oranges': 'mandarin',
        'juice': 'dole',
        'milk': 'whole'
    }
    return preferrences[item]

def words_from_text(text: str) -> list[str]:
    '''
        given a string of text returns a list of the words in the text, in order, 
        where the words are all lowercase. 
    '''

    return [w.strip().lower() for w in text.split(' ')]

def calc_frequencies(words: list[str]) -> dict[str, int]:
    '''
        Given a list of words return a dictionary,
        where the key are the (distinct) set of words in the list, 
        and the values are the number of occurances of that word.
    '''
    frequencies = {} # dict()
    for w in words:
        if w not in frequencies:
            frequencies[w] = 0
        frequencies[w] += 1
    return frequencies

def calc_frequencies2(words: list[str]) -> dict[str, int]:
    '''
        Given a list of words return a dictionary,
        where the key are the (distinct) set of words in the list, 
        and the values are the number of occurances of that word.
    '''
    frequencies = {} # dict()
    for w in words:
        frequencies[w] = frequencies.get(w, 0) + 1
    return frequencies

def max_int_value_of_dict(dictionary: dict) -> int:
    max_value = 0
    for f in dictionary.values():
        if f > max_value:
            max_value = f
    return max_value

def set_words_by_frequecies(words: list[str], frequencies: dict[str, int], f: int) -> set[str]:
        word_set = set()
        for w in words:
            if frequencies[w] == f:
                word_set.add(w)
        return word_set

def top_N_entries(text: str, N: int) -> dict[str, int]:
    '''
        Given a text document consisting of any number of words (case insensetive), 
        return a dictionary with up to N elements,
        such that the keys are the frequencies, 
        and the values are the (lowercase) word, or words with that frequency.

        text = "Big Bob went to bob's house to meet Fred and Fred went to Bob's House but did not find Bob"

        top_N_entries(text, 1) = {3: 'to'}
        top_N_entries(entries, 2) = {3: 'to', 2: ['bob', 'bob's', 'fred', 'went']}
    '''

    # divide our text into a list of words
    words = words_from_text(text)

    # count the number of occurances of each word (as a dict)
    frequencies = calc_frequencies(words)

    # get max frequency (occurances) of any word
    max_frequency = max_int_value_of_dict(frequencies)

    # build a dict with the words corresponding to the top N frequencies
    topN = {}
    curr_f = max_frequency
    while len(topN) < N and curr_f > 0:
        set_of_words = set_words_by_frequecies(words, frequencies, curr_f)
        if len(set_of_words) == 1:
            topN[curr_f] = set_of_words.pop()
        elif len(set_of_words) > 1:
            list_of_words = list(set_of_words)
            list_of_words.sort()
            topN[curr_f] = list_of_words
        curr_f -= 1
    return topN

def ordered_by_frequencies_then_alpha(frequency_dict: dict[str, int]) -> list[str]:
    '''
        ordered_by_frequencies({'Bob': 1, 'Fred': 20, 'George': 13, 'Alice': 1}) = ['Fred', 'George', 'Alice', 'Bob']
    '''
    entries = list(frequency_dict.items())
    entries.sort(key=lambda x: (-x[1], x[0]))
    return [e[0] for e in entries]

def remove_values(num_list: list[int], val_to_remove: int) -> list[int]:   
    '''
        return a new list with the values from num_list, excluding the val_to_remove.

        remove_values([4, 2, 3, 2, 3 , 1, 7], 3) = [4, 2, 2, 1, 7]
    '''
    result_list = []
    for val in num_list:
        if val != val_to_remove:
            result_list.append(val)
    return result_list

def remove_values_in_place(num_list: list[int], val_to_remove: int) -> list[int]:
    '''
        return the existing list num_list, but first remove all entries with value equal to val_to_remove.

        num_list (before) = [4, 2, 3, 2, 3 , 1, 7]
        remove_values(num_list, 3) = [4, 2, 2, 1, 7]
        num_list (before) = [4, 2, 2, 1, 7]
    '''
    while True:
        try:
            num_list.remove(val_to_remove)
        except ValueError:
            return
