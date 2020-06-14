# decrypting a message when you don't know which key was used

message = "Dro aesmu lbygx pyh TEWZC yfob dro vkji nyq.".lower()
letters = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(message):
    for key in range(len(letters)): # 26 possible keys
        decrypted_messages = ""     # decrypted messages to return
        for symbol in message:      # for every character in the message
            if symbol in letters:   # if the character is alaphabetical
                num = letters.find(symbol)
                num -= key          # change it by the key number

                if num < 0:
                    num += len(letters)

                # add symbol to decrypted_message
                decrypted_messages += letters[num]
            else:
                # symbol is not alphabetic
                # add it to decrypted_message
                decrypted_messages += symbol

        print(decrypted_messages)

decrypt(message)
