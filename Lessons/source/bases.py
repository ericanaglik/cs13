#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

hex_dict = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g', '17' : 'h', '18': 'i', '19': 'j', '20': 'k',  '21': 'l', '22': 'm', '23': 'n', '24': 'o', '25': 'p', '26': 'q', '27': 'r', '28': 's', '29': 't', '30': 'u',  '31': 'v', '32': 'w', '33': 'x', '34': 'y', '35': 'z' }

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    digits_list = list(digits.lower())
    digits_list.reverse()
    # print(digits_list)
    # go through the array and figure out what each 1 and 0 mean
    total = 0
    for i, value in enumerate(digits_list):
        place_value = base ** i
        # print(place_value, value)
        total += digit_value[value] * place_value
        # print(place_value, digit_value[value], digit_value[value] * place_value, total)
    return total


    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    

    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    place = 1
    while place < number:
        place *= base
    place /= base
    return_list = []
    while place >= 1:
        digit_counter = 0
        while number - place >= 0:
            number -= place
            digit_counter += 1
        return_list.append(value_digit[digit_counter])
        place /= base   
    return ''.join(return_list)
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    decoded = decode(digits, base1)
    encoded = encode(decoded, base2)
    return encoded
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    result = decode(digits, base1)
    return encode(result, base2)
    # ...

def convert_fractional(digits, base1, base2):
    #12.35
    # begin with the decimal fraction and multiply by 2
    # grab the whole number from the result and add to the right of the point
    # convert to string
    # string split at decimal 
    # create a var for everything right of the decimal and then multiply by 2

    # split string at decimal
    digits = digits.split(".")
    # convert the whole number to binary 
    whole = convert(digits[0], 10, 2)

    # cleaning up decimal so I can convert to binary 
    deci = "." + digits[1]
    deci = float(deci)

    to_binary = ""
    
    while deci != 0:
        deci *= 2
        if deci >= 1:
            to_binary += "1"
            deci -= 1
        else:
            to_binary += "0"
    return whole + "." + to_binary


def convert_negative(digits, base1, base2):
    pass


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    print(convert_fractional(".625", 10, 2))

