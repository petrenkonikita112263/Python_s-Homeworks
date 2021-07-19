import string

ALPHABET = string.ascii_lowercase
ALPHABET_LIST = list(ALPHABET) + list(ALPHABET)


def encrypt(text: str, shift: int) -> str:
    '''
    INPUT: text as a string and an integer for the shift value.
    OUTPUT: The shifted text after being run through the Caeser cipher.
    '''
    output_message = ""
    for char in text:
        if char in ALPHABET_LIST:
            position = ALPHABET_LIST.index(char)
            new_position = position + shift
            output_message += ALPHABET_LIST[new_position]
        else:
            output_message += char
    return f"{output_message}, {shift}"


# Example:
print(encrypt('Get this message to the main server', 13))


# 'Grg guvf zrffntr gb gur znva freire'

def decrypt(text, shift):
    '''
    INPUT: A shifted message and the integer shift value
    OUTPUT: The plain text original message.
    '''
    output_message = ""
    shift *= -1
    for char in text:
        if char in ALPHABET_LIST:
            position = ALPHABET_LIST.index(char)
            new_position = position + shift
            output_message += ALPHABET_LIST[new_position]
        else:
            output_message += char
    return f"{output_message}, {shift}"


# Example:
print(decrypt('Grg guvf zrffntr gb gur znva freire', 13))


# 'get this message to the main server'

def brute_force(message):
    """
    INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message.
            One of the printed outputs should be readable.
    """
    for n in range(26):
        print(f"Using shift value of {n}")
        print(decrypt(message, n) + "\n")


brute_force('Grg guvf zrffntr gb gur znva freire')
