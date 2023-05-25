from tkinter import *
import Application_main
import re
import copy
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter.messagebox as mb
import SQL
from datetime import datetime
from functools import partial


def handle_click_btnInsert(event):  # Create function to handle btnInsert

    def clear():  # function to remove a character in the entered text
        try:
            Text.delete(text_entry, 0)
        except TclError:
            return 0

    def display():  # Function to display changed text
        global text_update
        text_update = ''
        text_update_for_searching = ''
        text = text_entry.get("1.0", "end-1c")
        text_list = text.split(' ')
        print(text_list)
        text_update = ''
        text_update_for_searching = ''
        text_list = text.split(' ')
        text_for_searching = copy.copy(text_list)
        text_for_searching = text.split(' ')
        for i in range(len(text_for_searching)):  # cleaning text from signes
            if re.search(r'\W', text_for_searching[i]):
                text_for_searching[i] = text_for_searching[i][:-1]

        text_update_for_searching = ' '.join(text_for_searching)  # getting "naked" text
        text_update_for_searching = text_update_for_searching.lower()  # making a lower
        text_update_for_searching = text_update_for_searching.split(' ')

        btn_word1=Button(master=text_output,activeforeground='red',
               bg = '#bec4da',activebackground='#bec4da',
               highlightthickness=1,bd = 0, font='Times')
        btn_word2=Button(master=text_output,activeforeground='red',
               bg = '#bec4da',activebackground='#bec4da',
               highlightthickness=1,bd = 0, font='Times')
        btn_word3=Button(master=text_output,activeforeground='red',
               bg = '#bec4da',activebackground='#bec4da',
               highlightthickness=1,bd = 0, font='Times')

        final_text_in_list = re.findall(r'[0-9]+|[A-z]+|"|!', str(text_list))  # copy text_list, without space and comma
        final_text_in_list = final_text_in_list[1:-1]
        for i in (range(len(text_update_for_searching))):  # in "naked" text searching right words
            if SQL.cast_verbs(text_update_for_searching[i]):
                btn_word1.config(text=re.findall(r'\w+',SQL.cast_verbs(text_update_for_searching[i]))[0])
                btn_word2.config(text=re.findall(r'\w+',SQL.cast_verbs(text_update_for_searching[i]))[1])
                btn_word3.config(text=re.findall(r'\w+',SQL.cast_verbs(text_update_for_searching[i]))[2])
                final_text_in_list[i] = SQL.cast_verbs(text_update_for_searching[i])  # return 3 or 4 words
                print()
                btn_word1.place(x=220,y=20)
                btn_word2.place(x=320,y=20)
                btn_word3.place(x=420,y=20)

        final_text = ''
        for el in final_text_in_list:  # making a text in normal str-format
            final_text += el + ' '
        print('text_update = ', text_update, '\n', final_text, sep='')

        text_update = ' '.join(text_list)
        text_output.delete(1.0, END)
        text_output.insert(1.0, final_text)
        text_entry.delete("1.0", "end-1c")  # Deletes all entered text when click display

    def exit_insert():  # Function to exit out of insert label
        destroy_all(text_entry, text_output, display_click_btnInsert, clear_click_btnInsert, btn_insert_exit,
                    scroll_entry, scroll_output)
        global click_btn_insert
        click_btn_insert = False

    def save_in_history():
        try:
            SQL.save_in_history(text_update, datetime.now())
            print(datetime.now())
            msg = 'Текст сохранен'
            mb.showinfo("Сохранение", msg)
        except NameError:  # if user didn't display a text - show a message
            msg = 'Введите текст'
            mb.showerror("Ошибка", msg)
            return 0

    global click_btn_insert
    # Set parameters for buttons
    click_btn_insert = False

    if not click_btn_insert:
        text_output = Text(height=20, width=88, bg='#bec4da', wrap=WORD, font='Times')
        text_entry = Text(height=20, width=88, bg='#bec4da', wrap=WORD, font='Times')
        scroll_entry = Scrollbar(command=text_entry.yview())
        scroll_output = Scrollbar(command=text_output.yview())

        text_output.pack(anchor='e', padx=49, pady=10)
        text_entry.pack(anchor='e', padx=49, pady=60)
        scroll_output.pack(side=LEFT, fill=Y)
        scroll_entry.pack(side=LEFT, fill=Y)
        text_output.config(yscrollcommand=scroll_output.set)
        text_entry.config(yscrollcommand=scroll_entry.set)

        btn4 = ImageTk.PhotoImage(file="pictures/little_Display.png")
        btn5 = ImageTk.PhotoImage(file="pictures/little_Clear.png")
        btn6 = ImageTk.PhotoImage(file="pictures/little_Close.png")
        btn7 = ImageTk.PhotoImage(file="pictures/little_Display.png")

        display_click_btnInsert = Button(text='Display', command=display)
        display_click_btnInsert.place(x=250, y=350)

        clear_click_btnInsert = Button(text='Clear', command=clear)
        clear_click_btnInsert.place(x=330, y=350)

        btn_insert_exit = Button(text='Close!', command=partial(exit_insert))
        btn_insert_exit.place(x=700, y=350)

        btn_insert_exit = Button(text='Save', command=save_in_history)
        btn_insert_exit.place(x=380, y=350)

        click_btn_insert = True


def destroy_all(*args):
    for i in args:
        i.destroy()


def handle_click_btnRandom(event):
    def handle_click_on_theme(theme):
        destroy_all(label_theme, btnNature, btnSocial, btnTechnology)
        text = Text(height=20, width=88, bg='#bec4da', wrap=WORD)
        text.pack(anchor='e', padx=49, pady=10)
        text.insert(1.0, (SQL.get_text_by_theme([theme])))

    label_theme = Label(background='#d7ebf4', width=20, height=200, text='Themes', font='Bold', anchor='n',
                        pady=10)  # create add. side for different themes
    label_theme.pack()
    label_theme.place(x=200)
    Nature, Social, Technology = 'Nature', 'Social', 'Technology'  # list of topics
    btnNature = Button(text=Nature, command=partial(handle_click_on_theme,
                                                    Nature))  # when the user selects, the text on this topic will be displayed
    btnSocial = Button(text=Social, command=partial(handle_click_on_theme, Social))
    btnTechnology = Button(text=Technology, command=partial(handle_click_on_theme, Technology))
    btnNature.pack()
    btnSocial.pack()
    btnTechnology.pack()
    btnNature.place(x=200, y=30)
    btnSocial.place(x=200, y=60)
    btnTechnology.place(x=200, y=90)


def handle_click_btnHome(event):  # Create function to handle btnHome
    with open('home.txt', 'r') as file:
        home_text = file.read()  # Open and read file home.txt
    try:
        home_label = Label(text=home_text, anchor='n')
        home_label_btn_close = Button(home_label, text='Закрыть', anchor='s', command=home_label.destroy)
        # home_label.grid(row=100, column=59)
        home_label.pack()
        home_label_btn_close.pack(padx=200, pady=100)

    except Tk.report_callback_exception as ex:
        print('Error!', ex)


def handle_click_btnHistory(event):  # create a table with date and your previos texts
    # data
    ls = SQL.return_text_for_history()
    print(ls)

    columns = ("text", "date")

    tree = ttk.Treeview(columns=columns, show="headings", height=200)
    # tree.grid(sticky = 'we',column=1,row=1)
    tree.pack(side=RIGHT)

    # table's head
    tree.heading("text", text="text")
    tree.heading("date", text="date")

    tree.column("#1", stretch=YES, width=600)
    tree.column("#2", stretch=YES, width=200)

    # data
    for text in ls:
        tree.insert("", END, values=text)
