import tkinter.font
from tkinter import *
import random
import re
import copy
from PIL import ImageTk, Image
from tkinter import ttk
from datetime import datetime
from functools import partial
from Main import *
from datetime import datetime
import json


def handle_click_btnInsert():  # Create function to handle btnInsert

    def clear():  # function to remove a character in the entered text
        try:
            Text.delete(text_entry, 0)
        except TclError:
            return 0

    def exit_insert(*args):  # Function to exit out of insert label
        destroy_all(*args)
        btn_insert_exit.destroy()
        global click_btn_insert
        click_btn_insert = False

    def display():  # Function to display changed text
        # text_update = ''
        text = text_entry.get("1.0", "end-1c").lower()  # Get string from text_entry. Make them in lower case
        text_list = text.replace('.', '|.').replace('!', '|!').replace('?', '|?').replace(',', '|,').replace(' ',
                                                                                                             '|').split(
            '|')  # Create list of enter words

        with open('all_verbs.json', 'r', encoding='utf-8') as f:  # Joined regular and irregular verbs in all_verbs.json
            words_list = json.load(f)

        for i in range(len(words_list)):  # Looping through all the words in the words_list
            for j in range(len(text_list)):
                if text_list[j] in words_list[i]:  # If entered words matched with word_list, replace this words to list of verbs
                    text_list[j] = ' '.join(words_list[i])

        new_text = ' '.join(text_list).replace(' ?', '?').replace(' .', '.').replace(' ,', ',').replace(' !',
                                                                                                        '!')  # Return string from list of enter words
        text_output.insert(1.0, new_text.capitalize())  # Return changed and capitalize string
        # text_entry.delete(text_entry, 0)  # Deletes all entered text when click display
        with open('words.txt', 'a', encoding='utf-8') as file:  # Save string in words.txt with current datetime
            file.write(f"{new_text.capitalize()} \t {''.join(str(datetime.now()))}\n")


    global click_btn_insert
    click_btn_insert = False
    if not click_btn_insert:  # if the button is not pressed, the process starts
        text_output = Text(height=17, width=68, bg='#bec4da', wrap=WORD, font='Times')

        text_entry = Text(height=17, width=88, bg='#bec4da', wrap=WORD, font='Times')  # Create window to input text
        right_frame = Text(height=17, width=18, bg='#bec4da', wrap=WORD, font='Times')

        text_output.place(y=35, x=240)
        text_entry.place(y=435, x=240)
        right_frame.place(x=800, y=35)
        text_entry = Text(height=17, width=88, bg='#bec4da', wrap=WORD, font='Times')
        right_frame = Canvas(height=323, width=147, bg='#bec4da')

        text_output.place(y=35, x=240)
        text_entry.place(y=435, x=240)
        right_frame.place(x=800, y=35)



        btn4 = ImageTk.PhotoImage(file="pictures/little_Display.png")
        btn5 = ImageTk.PhotoImage(file="pictures/little_Clear.png")
        btn6 = ImageTk.PhotoImage(file="pictures/little_Close.png")
        btn7 = ImageTk.PhotoImage(file="pictures/little_Display.png")

        # Set parameters for buttons
        display_click_btnInsert = Button(text='Запуск', command=display)
        clear_click_btnInsert = Button(text='Очистить', command=clear)
        btn_insert_exit = Button(text='Закрыть',
                                 command=partial(exit_insert, text_entry, text_output, display_click_btnInsert,
                                                 clear_click_btnInsert))
        btn_insert_save = Button(text='Save')

        display_click_btnInsert = Button(text='Display', command=display)

        display_click_btnInsert.place(x=250, y=385)
        clear_click_btnInsert.place(x=330, y=385)
        btn_insert_exit.place(x=700, y=385)
        btn_insert_save.place(x=405, y=385)

        click_btn_insert = True


def destroy_all(*args):
    for i in args:
        i.destroy()


def handle_click_btnRandom(event):

    canvas_theme = Canvas(background='#d7ebf4', width=150, height=800)
    canvas_theme.place(x=200)
    label_theme = Label(canvas_theme, background='#d7ebf4', text='Themes', font=('Times', 15, tkinter.font.BOLD),
                        anchor='n')  # create add. side for different themes
    label_theme.place(x=30)
    Nature, Social, Technology = 'Nature', 'Social', 'Technology'  # list of topics
    btnNature = Button(text=Nature)  # when the user selects, the text on this topic will be displayed
    btnSocial = Button(text=Social)
    btnTechnology = Button(text=Technology)
    btnNature.pack()
    btnSocial.pack()
    btnTechnology.pack()
    btnNature.place(x=200, y=30)
    btnSocial.place(x=200, y=60)
    btnTechnology.place(x=200, y=90)


def handle_click_btnHistory(event):
    pass


def handle_click_btnHome():  # Create function to handle btnHome
    def exit_home():  # Function to exit out of home label
        global click_btn_home
        click_btn_home = False
        home_label.destroy()

    global click_btn_home
    click_btn_home =  False
    if not click_btn_home:
        with open('home.txt', 'r') as file:
            home_text = file.read()  # Open and read file home.txt
        try:
            home_label = Label(text=home_text, anchor='n')
            home_label_btn_close = Button(home_label, text='Закрыть', anchor='s', command=exit_home)
            home_label.place(x=370, y=200)
            home_label_btn_close.pack(padx=200, pady=100)
            click_btn_home = True
        except Tk.report_callback_exception as ex:
            print('Error!', ex)


