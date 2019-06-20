#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern == "":
        return True

    found = False
    text_index = 0
    pattern_index = 0
    match = 0

    while text_index <= len(text)-1 and found is False:
    
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                match = text_index
            if pattern_index == len(pattern)-1:
                found = True
            text_index += 1
            pattern_index += 1
        else:
            if pattern_index > 0:
                text_index = match + 1
            else:
                text_index += 1
            pattern_index = 0
    return found


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    found = None
    text_index = 0
    pattern_index = 0
    match = 0

    if pattern == "":
        return match
    
    while text_index <= len(text)-1 and found is None:
    
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                match = text_index
            if pattern_index == len(pattern)-1:
                found = match
            text_index += 1
            pattern_index += 1
        else:
            if pattern_index > 0:
                text_index = match + 1
            else:
                text_index += 1
            pattern_index = 0
    return found


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    # found = None
    # text_index = 0
    # pattern_index = 0
    # match = 0
    # indexes = []

    indexes = []

    if pattern == "":
        i = 0
        while i <= len(text)-1:
            indexes.append(i)
            i += 1
        return indexes

    for index, letter in enumerate(text):
        if pattern == "":
            return indexes
        if letter == pattern[0]:
            if text[index: index + len(pattern)] == pattern:
                indexes.append(index)
            else: continue

    return indexes


    # 
    
    # while text_index <= len(text)-1:
    #     if text[text_index] == pattern[pattern_index]:
    #         if pattern_index == 0:
    #             match = text_index
    #         if pattern_index == len(pattern)-1:
    #             indexes.append(match)
    #         text_index += 1
    #         pattern_index += 1
    #     else:
    #         if pattern_index > 0:
    #             text_index = match + 1
    #         else:
    #             text_index += 1
    #         pattern_index = 0
    # return indexes


def test_string_algorithms(text, pattern):
    # found = contains(text, pattern)
    # print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    print(find_all_indexes('abc', 'a'))
