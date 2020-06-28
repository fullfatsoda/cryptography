message = "Dro aesmu lbygx pyh tewzc yfob dro vkji nyq."


def decrypt(message, key):
    key = -key
    decrypted_message = ""      # decrypted message to return
    for symbol in message:      # for every character in the message
        if symbol.isalpha():    # if the character is alaphabetical
            num = ord(symbol)   # set numerical value to character
            num += key          # change it by the key number

            # 26 is the highest value in the alphabet depending on the key
            # num needs to 'wrap back around' to the start of the alphabet
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            # add symbol to decrypted_message
            decrypted_message += chr(num)
        else:
            # symbol is not alphabetic
            # add it to decrypted_message
            decrypted_message += symbol

    return decrypted_message


print(decrypt(message, 10))
