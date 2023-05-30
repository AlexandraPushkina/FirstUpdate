import tkinter.font
from tkinter import *
import random
import Application_main
import re
import copy
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter.messagebox as mb
import SQL
from datetime import datetime
from functools import partial


def handle_click_btnInsert(event, from_random, random_text):  # Create function to handle btnInsert

    def clear():  # function to remove a character in the entered text
        try:
            Text.delete(text_entry, 0)
        except TclError:
            return 0

    def display(random_text):  # Function to display changed text
        global text_update
        text_update = ''
        text_update_for_searching = ''
        if random_text:
            text = random_text
        else:
            text = text_entry.get("1.0", "end-1c")
        text_list = text.split(' ')
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

        final_text_in_list = re.findall(r'[0-9]+|[A-z]+|"|!', str(text_list))  # copy text_list, without space and comma
        final_text_in_list = final_text_in_list[1:-1]
        for i in (range(len(text_update_for_searching))):  # in "naked" text searching right words
            if SQL.cast_verbs(text_update_for_searching[i]):
                create_radio_button(re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[0],
                                    re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[1],
                                    re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[2])
                final_text_in_list[i] = '(...,...,...)'  # return 3 or 4 words

        final_text = ''
        for el in final_text_in_list:  # making a text in normal str-format
            final_text += el + ' '

        text_update = ' '.join(text_list)
        text_output.delete(1.0, END)
        text_output.insert(1.0, final_text)
        text_entry.delete("1.0", "end-1c")  # Deletes all entered text when click display

    def create_radio_button(word1, word2, word3):
        global count
        count = 1
        array = [word1, word2, word3]
        random.shuffle(array)
        print(array[0])
        choice1 = Button(master=right_frame, activeforeground='red',
                         bg='#bec4da', activebackground='#bec4da',
                         highlightthickness=1, bd=0, font='Times',
                         text=array[0])
        choice2 = Button(master=right_frame, activeforeground='red',
                         bg='#bec4da', activebackground='#bec4da',
                         highlightthickness=1, bd=0, font='Times',
                         text=array[1])
        choice3 = Button(master=right_frame, activeforeground='red',
                         bg='#bec4da', activebackground='#bec4da',
                         highlightthickness=1, bd=0, font='Times',
                         text=array[2])
        choice1.pack()
        choice2.pack()
        choice3.pack()
        count+=30

    def exit_insert():  # Function to exit out of insert label
        destroy_all(text_entry, text_output, display_click_btnInsert, clear_click_btnInsert, btn_insert_exit)
        global click_btn_insert
        click_btn_insert = False

    def save_in_history():
        try:
            SQL.save_in_history(text_update, datetime.now())
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
        text_output = Text(height=17, width=68, bg='#bec4da', wrap=WORD, font='Times')
        text_entry = Text(height=17, width=88, bg='#bec4da', wrap=WORD, font='Times')
        right_frame = Canvas(height=323, width=147, bg='#bec4da',scrollregion=(-1000,-1000,1000,1000))

        text_output.place(y=35, x=240)
        text_entry.place(y=435, x=240)
        right_frame.place(x=800, y=35)


        btn4 = ImageTk.PhotoImage(file="pictures/little_Display.png")
        btn5 = ImageTk.PhotoImage(file="pictures/little_Clear.png")
        btn6 = ImageTk.PhotoImage(file="pictures/little_Close.png")
        btn7 = ImageTk.PhotoImage(file="pictures/little_Display.png")


        display_click_btnInsert = Button(text='Display', command=partial(display, False))
        display_click_btnInsert.place(x=250, y=385)

        clear_click_btnInsert = Button(text='Clear', command=clear)
        clear_click_btnInsert.place(x=330, y=385)

        btn_insert_exit = Button(text='Close!', command=partial(exit_insert))
        btn_insert_exit.place(x=700, y=385)

        btn_insert_exit = Button(text='Save', command=save_in_history)
        btn_insert_exit.place(x=380, y=385)

        click_btn_insert = True

        if from_random:
            display(random_text)


def destroy_all(*args):
    for i in args:
        i.destroy()


def handle_click_btnRandom(event):
    # try:
    #     destroy_all(text)
    # except NameError:
    #     pass
    def handle_click_on_theme(theme):
        destroy_all(label_theme, canvas_theme, btnNature, btnSocial, btnTechnology)
        handle_click_btnInsert(1, True, (SQL.get_text_by_theme([theme])))
        # text = Text(height=20, width=88, bg='#bec4da', wrap=WORD)
        # text.pack(anchor='e', padx=49, pady=10)
        # text.insert(1.0, )
        # handle_click_btnInsert(1, text)

    canvas_theme = Canvas(background='#d7ebf4', width=150, height=800)
    canvas_theme.place(x=200)

    label_theme = Label(canvas_theme, background='#d7ebf4', text='Themes', font=('Times', 15, tkinter.font.BOLD),
                        anchor='n')  # create add. side for different themes
    label_theme.place(x=30)
    Nature, Social, Technology = 'Nature', 'Social', 'Technology'  # list of topics
    btnNature = Button(canvas_theme, text=Nature, command=partial(handle_click_on_theme,
                                                                  Nature))  # when the user selects, the text on this topic will be displayed
    btnSocial = Button(canvas_theme, text=Social, command=partial(handle_click_on_theme, Social))
    btnTechnology = Button(canvas_theme, text=Technology, command=partial(handle_click_on_theme, Technology))
    btnNature.place(y=30)
    btnSocial.place(y=60)
    btnTechnology.place(y=90)


def handle_click_btnHistory(event):  # create a table with date and your previos texts
    # data
    ls = SQL.return_text_from_history(user_id)

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


# def handle_click_btnConfirm(event):


def handle_click_btnNewUser():  # может сделать функцию по созданию начальных виджетов? Второй раз вызываем

    def sql_new_user():
        SQL.register_new_user(entry_name.get(), entry_password.get())
        msg = 'Вы зарегистированы'
        mb.showinfo("Сохранение", msg)
        destroy_all(top_canvas, main_label, name_label, password_label, entry_password, entry_name, btnConfirm)

    top_canvas = Canvas(width=1000, height=1000, bg='#31343f', highlightthickness=0)
    top_canvas.place(width=1000, height=800)

    main_label = Label(top_canvas, bg='#31343f', text='Sign Up', font=('Times', 30, 'bold'), fg='#bec4da')
    main_label.place(y=200, x=390)

    name_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font=('Times,6'), text='name')
    password_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font=('Times,6'), text='password')
    name_label.place(y=265, x=370)
    password_label.place(y=296, x=340)

    entry_name = Entry(master=top_canvas)
    entry_password = Entry(master=top_canvas)
    entry_name.place(x=450, y=270)
    entry_password.place(x=450, y=300)

    btnBack = Button(top_canvas, fg='#bec4da', bg='#31343f', activebackground='#31343f',
                     text='Back', font=('Times,4,highlight'), highlightthickness=1,
                     bd=0, command=partial(handle_main_window, 1))
    btnBack.place(y=380, x=440)

    btnConfirm = Button(master=top_canvas, text='Confirm', font=('Times,6'), width=10, height=1, command=sql_new_user)
    str = ''
    str = entry_name.get()
    btnConfirm.place(y=345, x=450)


def confirm_user(name, password, a, b, c, d, e, f, g, h):
    global user_id
    user_id = SQL.confirm_user(name, password)
    if user_id:
        destroy_all(a, b, c, d, f, e, g, h)
        welcome_user = Label(fg='#bec4da', bg='#151d39', font=('Times', 16, 'bold'),
                             text='Welcome back, \n' + SQL.return_user_name(user_id), width=13)
        welcome_user.place(x=20, y=20)


def handle_main_window(event):
    top_canvas = Canvas(width=1000, height=1000, bg='#31343f', highlightthickness=0)
    top_canvas.place(width=1000, height=800)

    main_label = Label(top_canvas, bg='#31343f', text='ABC-helper', font=('Times', 30, 'bold'), fg='#bec4da')
    main_label.place(y=200, x=390)

    name_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font=('Times,6'), text='name')
    password_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font=('Times,6'), text='password')
    name_label.place(y=265, x=370)
    password_label.place(y=296, x=340)

    with open('home.txt', 'r') as file:
        home_text = file.read()  # Open and read file home.txt
    try:
        home_label = Label(top_canvas, text=home_text, anchor='n', bg='#31343f', font=('Times', 15, 'bold'),
                           fg='#bec4da')
        home_label.place(x=180)
    except Tk.report_callback_exception as ex:
        print('Error!', ex)

    btnNewUser = Button(top_canvas, fg='#bec4da', bg='#31343f', activebackground='#31343f',
                        text='New user here?', font=('Times,4,highlight'), highlightthickness=1,
                        bd=0, command=handle_click_btnNewUser)
    btnNewUser.place(y=380, x=440)

    entry_name = Entry(master=top_canvas)
    entry_password = Entry(master=top_canvas, show='*')
    entry_name.place(x=450, y=270)
    entry_password.place(x=450, y=300)

    def return_entry():
        confirm_user(entry_name.get(), entry_password.get(), top_canvas, main_label, name_label, password_label,
                     btnNewUser, entry_password, entry_name, home_label)

    btnConfirm = Button(top_canvas, text='Confirm', font=('Times,6'), width=10, height=1,
                        command=return_entry)
    btnConfirm.place(y=345, x=450)
