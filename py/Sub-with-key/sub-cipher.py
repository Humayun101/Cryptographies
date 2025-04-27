def dec_sub(cipher, key):
    key = key.upper()
    plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decode_mapping = {key[i]: plain[i] for i in range(26)}
    
    plaintext = ''
    for char in cipher:
        if char.isalpha():
          
            if char.isupper():
                plaintext += decode_mapping.get(char, char)
            else:
                plaintext += decode_mapping.get(char.upper(), char).lower()
        else:
            plaintext += char
    
    return plaintext

key = input("ENTER KEY OF 26 ALPHABETS TO MAP TOWARD ENCRYPTION: ")
cipher = input("Input your cipher text: ")
plaintext = dec_sub(cipher, key)
print(plaintext)
