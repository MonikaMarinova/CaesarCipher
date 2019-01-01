"""
Application for encrypting and decrypting text using Caesar's Cipher
Problem covering algorithmic and security bases, creating UI from scratch
Implemented  by: Monika Marinova
"""
from tkinter import *


# Global variables for defining the range of lower case latin alphabet based on ASCII table
ascii_lower_a = 97
ascii_lower_z = 122
# Global variable for defining the number of letters in latin alphabet
number_of_letters = 25
# creating a window
root = Tk()
# creating a Global Text widget for displaying result values
text_output = Text(root, height=2, width=30)


def cc_gui():
    """
    Function in which is implemented simple UI
    :return: None
    """
    # creating labels
    hello_cc_label = Label(root, text=" Hi, this is Caesar's Cipher")
    text_lbl = Label(root, text="Insert text here:")
    key_lbl = Label(root, text="Insert key between 1 and 25:")
    text_output_lbl = Label(root, text="Result: ")

    # creating entries
    text_entry = Entry(root)
    key_entry = Entry(root)

    # creating buttons
    encryption_button = Button(root, text="Encrypt")
    decryption_button = Button(root, text="Decrypt")

    # grid layout
    hello_cc_label.grid(row=0, sticky=W)
    text_lbl.grid(row=1, sticky=E)
    key_lbl.grid(row=2, sticky=E)
    text_output_lbl.grid(row=3, sticky=E)
    text_entry.grid(row=1, column=1)
    key_entry.grid(row=2, column=1)
    text_output.grid(row=3, column=1)
    encryption_button.grid(row=6, column=0)
    decryption_button.grid(row=6, column=1)

    # binding
    #encryption_button.bind("<Button-1>", encrypt(text_entry.get(), key_entry.get()))
    #decryption_button.bind("<Button-1>", decrypt(text_entry.get(), key_entry.get()))

    encryption_button.bind("<Button-1>", encrypt("aa",12))
    decryption_button.bind("<Button-1>", decrypt("BB", 7))

    root.mainloop()


def key_in_range(key):
    """
    Function for checking if provided key is within range between 1 and 25
    :param key: string
    :return: bool
    """
    return 1 >= int(key) <= 25


def encrypt(text, key):
    """
    Function which implements encryption using Caesar's Cipher
    :param text:string
    :param key: string
    :return None
    """

    if key_in_range(key):
        # removing white spaces from the input text, creating a list
        phrase = list(''.join(text.split()))
        # creating variable for saving the final result
        encrypted_phrase = ""

        for character in phrase:
            # casting character to integer based on ASCII enumeration and shifting its position forward with key
            encrypted_character = ord(character) + int(key)
            # check if encrypted character is sill in the range of lower case latin alphabet
            if encrypted_character > ascii_lower_z:
                # if not: character is shifted back with 26(number of letters in latin alphabet + 1 to make it shift
                # from its original value)
                encrypted_character -= number_of_letters + 1
            # adding encrypted character to the result phrase
            encrypted_phrase += chr(encrypted_character)

        text_output.insert(END, encrypted_phrase)

    else:
        text_output.insert(END, "Key must be between 1 and 25!")



def decrypt(encrypted_text, key):
    """
    Function which implements decryption using Caesar's Cipher
    :param encrypted_text: string
    :param key: string
    :return None
    """

    if key_in_range(key):
        # creating a list from input text
        phrase = list(encrypted_text)
        # creating variable for saving the final result
        decrypted_phrase = ""

        for character in phrase:
            # casting character to integer based on ASCII enumeration and shifting its position backward with key
            decrypted_character = ord(character) - int(key)
            # check if encrypted character is sill in the range of lower case latin alphabet
            if decrypted_character < ascii_lower_a:
                # if not: character is shifted forward with 26(number of letters in latin alphabet + 1 to make it shift
                # from its original value)
                decrypted_character += number_of_letters + 1
            # adding decrypted character to the result phrase
            decrypted_phrase += chr(decrypted_character)

        text_output.insert(END, decrypted_phrase)
    else:
        text_output.insert(END, "Key must be between 1 and 25!")


if __name__ == '__main__':
    cc_gui()

