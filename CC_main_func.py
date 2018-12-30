"""
Console application for encrypting and decrypting text using Caesar's Cipher
Problem covering algorithmic and security bases
Implemented  by: Monika Marinova
"""

# Global variables for defining the range of lower case latin alphabet based on ASCII table
ascii_lower_a = 97
ascii_lower_z = 122
# Global variable for defining the number of letters in latin alphabet
number_of_letters = 25


def encrypt(text, key):
    """
    Function which implements encryption using Caesar's Cipher
    input: string, int
    return: string
    """
    # removing white spaces from the input text, creating a list
    phrase = list(''.join(text.split()))
    # creating variable for saving the final result
    encrypted_phrase = ""

    for character in phrase:
        # casting character to integer based on ASCII enumeration and shifting its position forward with key
        encrypted_character = ord(character) + key
        # check if encrypted character is sill in the range of lower case latin alphabet
        if encrypted_character > ascii_lower_z:
            # if not: character is shifted back with 26(number of letters in latin alphabet + 1 to make it shift from
            # its original value)
            encrypted_character -= number_of_letters + 1
        # adding encrypted character to the result phrase
        encrypted_phrase += chr(encrypted_character)

    return encrypted_phrase


def decrypt(encrypted_text, key):
    """
    Function which implements decryption using Caesar's Cipher
    input: string, int
    return: string
    """
    # creating a list from input text
    phrase = list(encrypted_text)
    # creating variable for saving the final result
    decrypted_phrase = ""

    for character in phrase:
        # casting character to integer based on ASCII enumeration and shifting its position backward with key
        decrypted_character = ord(character) - key
        # check if encrypted character is sill in the range of lower case latin alphabet
        if decrypted_character < ascii_lower_a:
            # if not: character is shifted forward with 26(number of letters in latin alphabet + 1 to make it shift from
            # its original value)
            decrypted_character += number_of_letters + 1
        # adding decrypted character to the result phrase
        decrypted_phrase += chr(decrypted_character)

    return decrypted_phrase


def caesar_cipher():
    """
    Function which acts as UI for using the implemented encryption and decryption methods
    input: None
    return: None
    """
    # infinite loop wic makes possible more than one operation in a run
    while(True):
        print("---Caeser's Cipeper:"
              " Please choose: \n"
              " - e: encryption \n"
              " - d: decryption \n"
              " - q: quit \n")
        choice = input()

        # option for quit
        if choice.lower() == 'q':
            print("Quit!")
            break

        # option for encryption
        elif choice.lower() == 'e':
            print("Please input text for encryption: ")
            input_text = input()
            print("Please input key between 1 and 25: ")
            input_key = int(input())
            if input_key < 1 or input_key > 25:
                print("Key must be between 1 and 25, encryption failed!")
                continue
            else:
                print(encrypt(input_text, input_key))

        # option for decryption
        elif choice.lower() == 'd':
            print("Please input text for decryption: ")
            input_text = input()
            print("Please input key between 1 and 25: ")
            input_key = int(input())
            if input_key < 1 or input_key > 25:
                print("Key must be between 1 and 25, decryption failed!")
                continue
            else:
                print(decrypt(input_text, input_key))

        # in any other case execution will be stopped
        else:
            print("Wrong input!")
            break


if __name__ == '__main__':
    caesar_cipher()
