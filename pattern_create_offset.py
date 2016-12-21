def create_pattern(length):


    uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    lowercase_chars = 'abcdefghijklmnopqrstuvxyz'
    number_chars = '0123456789'

    x = y = z = 0
    pattern = ''

    while True:



        if len(pattern) < length:
            pattern += uppercase_chars[x]
        if len(pattern) < length:
            pattern += lowercase_chars[y]
        if len(pattern) < length:
            pattern += number_chars[z]
        if len(pattern) == length:
            return pattern

        z += 1

        if x is 24:
            print ('[!] Maximum number of characters. Returning '
                   + str(len(pattern)) + ' characters!')
            return pattern
        if y is 24:
            y = 0
            x += 1
        if z is 10:
            z = 0
            y += 1


def find_offset(string):

    pattern = create_pattern(17286)

    if string in pattern:
        index = pattern.index(string)
        return index
    else:
        return False
