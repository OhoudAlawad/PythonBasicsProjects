##Create a code generator. Create 2 functions , the first one takes text as input,
#replaces each letter with another letter, and outputs the “encoded” message. , the
#second one decode the message to the original text

shift = 6



def encode(text):
    encryption= ""
    for i in text:
        if i.isupper():

            # find the position in 0-25
            unicode = ord(i)

            index = ord(i) - ord("A")

            # perform the shift
            new_index = (index + shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to encrypted string
            encryption = encryption + new_character

        else:

            # since character is not uppercase, leave it as it is
            encryption += i
    print("********************")    
    print("Plain text:",text)
    print("********************")
    print("Encrypted text:",encryption)

    decode(encryption)
        


def decode(cipher):
    plain_text = ""
    for i in cipher:

        # check if character is an uppercase letter
        if i.isupper():

            # find the position in 0-25
            unicode = ord(i)

            index = ord(i) - ord("A")

            # perform the negative shift
            new_index = (index - shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to plain string
            plain_text = plain_text + new_character

        else:

            # since character is not uppercase, leave it as it is
            plain_text += i

    print("********************")

    print("Decrypted text:",plain_text)


print("Welcom to Text Encryption Tool")
print("----------------------------------------")
text = input("Enter Your Text to encode it\n")

encode(text)
