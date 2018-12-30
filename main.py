"""Console application for encrypting and decrypting text using Caesar's Cipher"""

#Global variables for defining the range of lower case latin alphabet based on ASCII table
ascii_lower_a = 97
ascii_lower_z = 122
#Global variable for defining the number of letters in latin alphabet
number_of_letters = 25


def encrypt(text, key):
    """
    Function which implements encryption using Caesar's Cipher
    input: string, int
    return: string
    """
    #removing white spaces from the input text, creating a list
    phrase = list(''.join(text.split()))
    #creating variable for saving the final result
    encrypted_phrase = ""

    for character in phrase:
        #casting caracter to integer based on ASCII enumeration and shifting its position forward with key
        encrypted_character = ord(character) + key
        #check if encrypted character is sill in the range of lower case latin alphabet
        if encrypted_character > ascii_lower_z:
            #if not: characer is shifted back with 26(number of letters in latin alpabet + 1 to make it shift from its
            #original value
            encrypted_character -= number_of_letters + 1
        #adding encrypted caracter to the result phrase
        encrypted_phrase += chr(encrypted_character)

    return encrypted_phrase

def decrypt(encripted_text, key):
    """
    Function which implements decryption using Caesar's Cipher
    input: string, int
    return: string
    """
    #creating a list from input text
    phrase = list(encripted_text)
    #creating variable for saving the final result
    decrypted_phrase = ""

    for character in phrase:
        #casting caracter to integer based on ASCII enumeration and shifting its position backward with key
        decrypted_character = ord(character) - key
        #check if encrypted character is sill in the range of lower case latin alphabet
        if decrypted_character < ascii_lower_a:
            #
            decrypted_character += number_of_letters + 1
        #adding decrypted caracter to the result phrase
        decrypted_phrase += chr(decrypted_character)

    return decrypted_phrase
#to do
#restrict input to be only between 1 and 25

print(encrypt("hello world", 25))
print(decrypt("gdkknvnqkc", 25))


