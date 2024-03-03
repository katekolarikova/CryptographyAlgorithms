import random

alphatbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def create_alphabet(s):
    # Convert the string into a list of characters
    char_list = list(s)

    n = len(char_list)
    # swap each char with another randomly selected char
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        char_list[i], char_list[j] = char_list[j], char_list[i]

    return ''.join(char_list)

def encrypt(my_alphabet, text, shift_amount):
    result = ""
    for char in text:
        if char in my_alphabet:
            result += my_alphabet[(my_alphabet.index(char) + shift_amount) % 26]
    print(result)
    return result

def decrypt(my_alphabet, text):
    for shift in range(1,26):
        result = ""
        for char in text:
            if char in my_alphabet:
                result += my_alphabet[(my_alphabet.index(char) - shift) % 26]

        print(f'shift: {shift}')
        print(result)

my_alphatbet = custom_shuffle_string(alphatbet)
print(my_alphatbet)
test = encrypt(my_alphatbet,'AHOJ',3)
decrypt(my_alphatbet,test)