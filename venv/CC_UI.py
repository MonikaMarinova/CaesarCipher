"""
User Interface implementation for Caeser's cipher solution
Implemented by: Monika Marinova
"""
from tkinter import  *
from CC_main_func import *


# creating a window
root = Tk()


# creating labels
hello_CC_label = Label(root, text = " Hi, this is Caesar's Cipher" )
text_lbl = Label(root, text = "Insert text here:")
key_lbl = Label (root, text = "Insert key between 1 and 25:")
text_output_lbl = Label(root, text = "Result: ")

#creating entries
text_entry = Entry(root)
key_entry = Entry(root)

# creating a Text widget for displqying result values
text_output = Text(root, height = 2, width = 30)

#creating buttons
encryption_button = Button(root, text = "Encrypt")
decryption_button = Button(root, text = "Decrypt")

# grid layout
hello_CC_label.grid(row = 0, sticky = W)
text_lbl.grid(row = 1, sticky = E)
key_lbl.grid(row = 2, sticky = E)
text_output_lbl.grid(row = 3, sticky = E)
text_entry.grid(row = 1, column = 1)
key_entry.grid(row = 2, column = 1)
text_output.grid(row = 3, column = 1)
encryption_button.grid(row = 6, column = 0)
decryption_button.grid(row = 6, column = 1)


root.mainloop()