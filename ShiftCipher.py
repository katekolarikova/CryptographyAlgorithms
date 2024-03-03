alphatbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(text, shift_amount):
    result = ""
    for char in text:
        if char in alphatbet:
            result += alphatbet[(alphatbet.index(char) + shift_amount) % 26]
    print(result)
    return result

def decrypt(text):
    for shift in range(1,26):
        result = ""
        for char in text:
            if char in alphatbet:
                result += alphatbet[(alphatbet.index(char) - shift) % 26]

        print(f'shift: {shift}')
        print(result)

test = encrypt('AHOJ',3)
decrypt("""SFEFONXYJSNPDGJWSJYNHPJGJEUJHSTXYNRNXYWTAXYANXAJYFNNMKAQJISNRMTPJONGZIJ
XUTQZUWFHTAFYSFWTISNZWFIUWTPDGJWSJYNHPTZFNSKTWRFHSNGJEUJHSTXYADUQDAFY
TERJRTWFSIFPYJWJUTIJUXFQNWJINYJQSZPNGQZPFXPNSYWFUWJENIJSYHJXPJMTXAFEZQJISN
MTMTPJOJFQTNXMFIFRHENPXFRUNTSFYGZIJQJYTXAPAJYSZMTXYNYUWFMFFTXYWFAF""")