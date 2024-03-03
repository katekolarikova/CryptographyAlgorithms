alphatbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vigenereEncrypt(text, keyword):
    result = ""
    char_counter = 0
    for char in text:
        if char in alphatbet:
            alphatbet_index = alphatbet.index(char)
            key = keyword[char_counter%len(keyword)]
            key_index = alphatbet.index(key)
            result += alphatbet[( alphatbet_index + key_index) % 26]
            char_counter+=1
    print(result)
    return result

def vigenereDecrypt(text, keyword):
    result = ""
    char_counter = 0
    for char in text:
        if char in alphatbet:
            alphatbet_index = alphatbet.index(char)
            key = keyword[char_counter%len(keyword)]
            key_index = alphatbet.index(key)
            result += alphatbet[( alphatbet_index - key_index) % 26]
            char_counter+=1
    print(result)
    return result

vigenereEncrypt("""SLUNECNEATEPLEPOCASICTVRTKEMPROZATIMKONCIVNASLEDUJICICHDVOUDNECHSEZATAH
NEVETSINUUZEMIZASAHNEDESTNAHORACHANASEVEROVYCHODEVEVSECHPOLOHACHSNIH
OVIKENDUBUDEPOLOJASNOTEPLOTYVNOCIKLESNOUPODNULUPRESDENBUDEMAXIMALNES
ESTSTUPNU""","ZIMA")

vigenereDecrypt("""RTGNDKZEZBQPKMBOBIEIBBHRSSQMOZAZZBUMJWZCHDZARTQDTRUCHKTDUWGDMMOHR
MLASITNDDQTRQZUTHQMHHMSZPZECMETMITOQIOHZVMSDDQRNDKCGWPEUMHSDKTPNT
AHZKTSMQTOUQWEMLGBTLQPNTAJZAZOSMBLNBKVMWOIJTQSMWGPNLZUKCBRDAPEMJG
DDUMXHUMLMMEERBETTXZU""", "ZIMA")
