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

#creating entries
text_entry = Entry(root)
key_entry = Entry(root)

#creating buttons
encryption_button = Button(root, text = "Encrypt")
decryption_button = Button(root, text = "Decrypt")

# grid layout
hello_CC_label.grid(row = 0)
text_lbl.grid(row = 1)
key_lbl.grid(row = 2)
text_entry.grid(row = 1, column = 1)
key_entry.grid(row = 2, column = 1)
encryption_button.grid(row = 6, column = 0)
decryption_button.grid(row = 6, column = 1)



root.mainloop()