from tkinter import *
from Main import *
from datetime import datetime

click_btn_insert = False
def handle_click_btnInsert(): # Create function to handle btnInsert

    def clear(): # function to remove a character in the entered text
        Entry.delete(text_enter, 0, END) # Deletes all entered text

    def display(): # Function to display changed text
        # text_update = ''
        text = text_enter.get() # Get string from text_enter
        text_list = text.split(' ') # Create list of enter words

        with open('regular_verbs.txt', 'r', encoding='utf-8') as f:
            word_list = f.read()
        
        for i in range(len(text_list)): # If entered words are in regular_verbs, change them on True
            if text_list[i] in word_list:
                text_list[i] = 'True' 

        new_text = ' '.join(text_list) # Return string from list of enter words

        text_label['text'] = new_text
        text_enter.delete(0, END) # Deletes all entered text when click display

        with open('words.txt', 'a', encoding='utf-8') as file:
            file.write(f"{new_text} \t {''.join(str(datetime.now()))}\n")

    def exit_insert(): # Function to exit out of insert label
        text_label.destroy()
        text_enter.destroy()
        display_click_btnInsert.destroy()
        clear_click_btnInsert.destroy()
        btn_insert_exit.destroy()
        global click_btn_insert
        click_btn_insert = False

    global click_btn_insert
    if not click_btn_insert: # if the button is not pressed, the process starts 
        text_label = Label() # Create window for text 
        text_enter = Entry() # Create window to input text
        text_enter.delete(0, END)
        text_label.pack(anchor=CENTER, padx=6, pady=6)
        text_enter.pack(anchor=CENTER, padx=6, pady=6)

        # Set parameters for buttons
        display_click_btnInsert = Button(text='Запуск', command=display)
        clear_click_btnInsert = Button(text='Очистить', command=clear)
        btn_insert_exit = Button(text='Закрыть', command=exit_insert)

        display_click_btnInsert.place(x=400, y=75)
        clear_click_btnInsert.place(x=460, y=75)
        btn_insert_exit.place(x=535, y=75)
        
        click_btn_insert = True


click_btn_home = False
def handle_click_btnHome(): # Create function to handle btnHome

    def exit_home(): # Function to exit out of home label
        global click_btn_home
        click_btn_home = False
        home_label.destroy()

    global click_btn_home
    if not click_btn_home:
        with open('home.txt', 'r') as file:
            home_text = file.read() # Open and read file home.txt
        try: 
            home_label = Label(text=home_text, anchor='n')
            home_label_btn_close = Button(home_label, text='Закрыть', anchor='s', command=exit_home)
            home_label.place(x=370, y=200)
            home_label_btn_close.pack(padx=200, pady=100)
            click_btn_home = True
        except Tk.report_callback_exception as ex:
            print('Error!', ex)
