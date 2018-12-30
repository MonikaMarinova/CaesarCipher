"""
User Interfase implementation for Caeser's cipher solution
Implemented by: Monika Marinova
"""
from tkinter import  *
from CC_main_func import *


# creating a window
root = Tk()

# creating and displaying a layout using frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

# creating and displaying labels
hello_CC_label = Label(topFrame, text = " Hi, this is Caesar's Cipher" )
hello_CC_label.pack(side = LEFT)
text_lbl = Label(topFrame, text = "Insert text here: ")
text_lbl.pack(side = LEFT)
key_lbl = Label (topFrame, text = "Insert key between 1 and 25")
key_lbl.pack(side = LEFT)

#creating and displaying buttons
encryption_button = Button(bottomFrame, text = "Encrypt")
encryption_button.pack(side = RIGHT)
decryption_button = Button(bottomFrame, text = "Decrypt")
decryption_button.pack(side = LEFT)

root.mainloop()