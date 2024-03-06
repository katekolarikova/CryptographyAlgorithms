alphatbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def create_key(s):
    # Initialize an array with the same length as the input string filled with None
    # to store the numbers.
    results = [None] * len(s)
    # Initialize the number to assign to 1.
    number = 1

    # Convert the string to lowercase to make the algorithm case-insensitive.
    s_lower = s.lower()

    # Iterate through each letter of the alphabet.
    for char in 'abcdefghijklmnopqrstuvwxyz':
        # Iterate through each character in the string.
        for i, letter in enumerate(s_lower):
            # If the letter matches the current alphabet letter and the position is not already filled.
            if letter == char and results[i] is None:
                # Assign the number to the corresponding index in the results array.
                results[i] = number
                # Increase the number for the next letter.
                number += 1

    # Return the results array filled with numbers.
    print(results)
    return results

def encrypt(text, key, desired_order):
    num_of_missing_chars = len(text) % len(key)

    # fill free posistions with X
    for i in range(0, num_of_missing_chars):
        text+='X'
    row_length = len(key)
    number_of_rows = len(text) // len(key)
    columns=[]

    # split text into columns
    for i in range(0, row_length):
        column = []

        # find characters for each column
        for j in range (0, number_of_rows):
            char = text[len(key)*j+i]
            if char in alphatbet:
                column.append(char)
            else:
                column.append('X')
        columns.append(column)

    # reorder columns

    reordered_columns = [columns[k-1] for k in desired_order]
    cipher_text = ""

    # create cipher text from reordered columns
    for column in reordered_columns:
        for char in column:
            cipher_text+=char
    print(cipher_text)

    return cipher_text

def decrypt(text, key, desired_order):
    row_length = len(key)
    number_of_rows = len(text) // len(key)
    columns = []

    # split text into columns
    for i in range(0, row_length):
        column = []

        # find characters for each column
        for j in range(0, number_of_rows):
            char = text[number_of_rows * i + j]
            if char in alphatbet:
                column.append(char)
        columns.append(column)
    back_to_order = []

    # key for decryption
    # array preparadet
    for number in range(1, max(desired_order)+1):
        back_to_order.append(0)

    # fill array with correct order ( look ath cypher key and find the index )
    for number in range(1, max(desired_order)+1):
        index = desired_order.index(number)
        back_to_order[number-1] = index + 1


    reordered_columns = [columns[k-1] for k in back_to_order]
    cipher_text = ""

    # create text - read appropriate string of each column
    for char  in range(0, number_of_rows):
        for column in reordered_columns:
            cipher_text += column[char]
    print(cipher_text)
    return cipher_text

desired_order = create_key('projev')
secret_message = """RUSKYPREZIDENTVLADIMIRPUTINPRONESLVECTVRTEKTRADICNIPROJEVOSTAVUFEDERACEVENOVALSETOMUZERUSKOMUSIPOKRACOVATVTRANSFORMACIANEMUZESESPOKOJITSESOUCASNYMSTAVEMZMINILSTOUPAJICIPOCETCHUDYCHIZAOSTALOUINFRASTRUKTURUNUTNOUPODPORUDUCHODCUMIMLADYMRODINYMABYSEZVRYTILNEPRIZNIVYDEMOGRAFICKYVYVOJ"""
test_messgae = "THESIMPLESTPOSSIBLETRANSPOSITIONSXX"
test = encrypt(secret_message, 'projev', desired_order)
decrypt(test, 'projev', desired_order )