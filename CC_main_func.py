"""
DOCSTRING:
Application for encrypting and decrypting text using Caesar's Cipher
Problem covering algorithmic and security bases, creating UI from scratch
Implemented  by: Monika Marinova
"""

import tkinter as tk

# Global variables are used so in case of reusing of code or adding Upper letters to be easily chengable
# Global variables for defining the range of lower case latin alphabet based on ASCII table
ascii_lower_a = 97
ascii_lower_z = 122
# Global variable for defining the number of letters in latin alphabet
number_of_letters = 25


class CCApp(tk.Tk):
    """
    DOCSTRING:
    Class in which is defined simple UI interface
    Several widgets are created and aligned into window form using grid alignment
    functions: on_enc_click, on_deck_click
    """

    # Constructor in which widgets are created and aligned in a window form
    def __init__(self):
        tk.Tk.__init__(self)
        # creating labels
        self.hello_cc_label = tk.Label(self, text=" Hi, this is Caesar's Cipher")
        self.text_lbl = tk.Label(self, text="Insert text here:")
        self.key_lbl = tk.Label(self, text="Insert key between 1 and 25:")
        self.text_output_lbl = tk.Label(self, text="Result: ")

        # creating a Text widget for displaying result values
        self.text_output = tk.Text(self, height=2, width=30)

        # creating entries and StringVars for getting entry values
        self.text_entry = tk.Entry(self)
        self.key_entry = tk.Entry(self)

        # creating and binding buttons to click methods
        self.encryption_button = tk.Button(self, text="Encrypt", command=self.on_enc_click)
        self.decryption_button = tk.Button(self, text="Decrypt", command=self.on_dec_click)

        # grid layout
        self.hello_cc_label.grid(row=0, sticky=tk.W)
        self.text_lbl.grid(row=1, sticky=tk.E)
        self.key_lbl.grid(row=2, sticky=tk.E)
        self.text_output_lbl.grid(row=3, sticky=tk.E)
        self.text_entry.grid(row=1, column=1)
        self.key_entry.grid(row=2, column=1)
        self.text_output.grid(row=3, column=1)
        self.encryption_button.grid(row=6, column=0)
        self.decryption_button.grid(row=6, column=1)

    def on_enc_click(self):
        """
        DOCSTRING:
        Click method for button encryption_button
        :param: self
        :return: NA
        """

        # deleting any previous text in Text widget
        self.text_output.delete("1.0", tk.END)
        # getting values which are user input for text and key
        text_entry_value = self.text_entry.get()
        key_entry_value = self.key_entry.get()
        # encrypted text is visualised into the text widget
        self.text_output.insert("1.0", encrypt(text_entry_value, key_entry_value))

    def on_dec_click(self):
        """
        DOCSTRING:
        Click method for button decryption_button
        :param: self
        :return: NA
        """

        # deleting any previous text in Text widget
        self.text_output.delete("1.0", tk.END)
        # getting values which are user input for text and key
        text_entry_value = self.text_entry.get()
        key_entry_value = self.key_entry.get()
        # encrypted text is visualised into the text widget
        self.text_output.insert("1.0", decrypt(text_entry_value, key_entry_value))


def encrypt(text, key):
    """
    DOCSTRING:
    Function which implements encryption using Caesar's Cipher
    :param text:string
    :param key: string
    :return string
    """

    # validating if the key is in the range between 1 and 25
    if 1 <= int(key) and 25 <= int(key):
        return "Key must be between 1 and 25!"
    else:
        # make the given string lower case
        text = text.lower()
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

        return encrypted_phrase


def decrypt(encrypted_text, key):
    """
    DOCSTRING:
    Function which implements decryption using Caesar's Cipher
    :param encrypted_text: string
    :param key: string
    :return string
    """

    # validating if the key is in the range between 1 and 25
    if 1 <= int(key) and 25 <= int(key):
        return "Key must be between 1 and 25!"
    else:
        # creating a list from lower case input text
        phrase = list(encrypted_text.lower())
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

        return decrypted_phrase


if __name__ == '__main__':
    # creating object of type CCApp
    app = CCApp()
    app.mainloop()

