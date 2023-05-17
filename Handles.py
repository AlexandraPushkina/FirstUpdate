import tkinter
from tkinter import *
from Main import *



def handle_click_btnInsert(event): # Create function to handle btnInsert



    def clear(): # function to remove a character in the entered text
        Entry.delete(text_enter, 0) 

    def display(): # Function to display changed text
        text = text_enter.get()
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        text_update = ''
        for i in range(len(text)):
            if text[i] in num_list:
                text_update += '1,2,3'
            else:
                text_update += text[i]

        text_label['text'] = text_update

    text_label = Label(height=20,width=100,anchor = 'e') # Create window for text
    text_enter = Entry(justify= tkinter.CENTER,width=50) # Create window to input text
    text_label.pack(anchor='e', padx=49, pady=6)
    text_enter.place(anchor=CENTER, height=60,x = 580, y =400)
    
    # Set parameters for buttons
    display_click_btnInsert = Button(text='Display', command=display)
    display_click_btnInsert.pack(side=LEFT, anchor=CENTER, padx=6, pady=6)

    clear_click_btnInsert = Button(text='Clear', command=clear)
    clear_click_btnInsert.pack(side=LEFT, anchor=CENTER, padx=6, pady=6)

def handle_click_btnHome(event): # Create function to handle btnHome
    canvas.delete                   # You must delete canvas
    with open('home.txt', 'r') as file:
        home_text = file.read() # Open and read file home.txt
    home_label = Label(text=home_text)
    home_label.grid(row=100, column=59)
    home_label.pack()

