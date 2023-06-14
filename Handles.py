from tkinter import *
from tkinter import ttk
import tkinter.font
from datetime import datetime
from functools import partial
import random
import re
import tkinter.messagebox as mb
import SQL
import translators as ts  # Module for translating (pip install translate-api, pip install translators --upgrade)


def handle_click_btnInsert(event, from_random, random_text):  # Create function to handle btnInsert

    def display(random_text):  # Function to display changed text
        def translate(text):
            text_entry.delete("1.0", "end-1c")
            text_translate = ts.translate_text(text, from_language='en',
                                               to_language='ru')  # Create translate entered text
            text_entry.insert(1.0, text_translate + '\n')  # Display translating text

        global list_of_correct_words
        global text_update
        list_of_correct_words = []
        miss_count = 1
        text_update = ''
        if random_text:
            text = random_text
        else:
            text = text_entry.get("1.0", "end-1c")
        text_list = text.split(' ')
        text_for_searching = text.split(' ')
        for i in range(len(text_for_searching)):  # cleaning text from signes
            if re.search(r'\W', text_for_searching[i]):
                text_for_searching[i] = text_for_searching[i][:-1]

        text_update_for_searching = ' '.join(text_for_searching)  # getting "naked" text
        text_update_for_searching = text_update_for_searching.lower()  # making a lower
        text_update_for_searching = text_update_for_searching.split(' ')

        final_text_in_list = re.findall(r'[0-9]+|[A-z]+|"|!',
                                        str(text_list))  # copy text_list, without space and comma
        final_text_in_list = final_text_in_list[1:-1]
        for i in (range(len(text_update_for_searching))):  # in "naked" text searching right words
            if SQL.cast_verbs(text_update_for_searching[i]):
                if len(SQL.cast_verbs(text_update_for_searching[i]).split()) == 4:  # if quantity of words is 4
                    list_of_correct_words.append(text_update_for_searching[i])
                    insert_listbox(re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[0],
                                   re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[1],
                                   re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[2],
                                   re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[3],
                                   miss_count=miss_count)  # add 4 words
                else:
                    list_of_correct_words.append(text_update_for_searching[i])
                    insert_listbox(re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[0],
                                   re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[1],
                                   re.findall(r'\w+', SQL.cast_verbs(text_update_for_searching[i]))[2],
                                   miss_count=miss_count)
                final_text_in_list[i] = '(...,...,...)'  # replace in text
                miss_count += 1  # how many missing words

        final_text = ''
        for el in final_text_in_list:  # making a text in normal str-format
            final_text += el + ' '

        text_update = ' '.join(text_list)
        text_output.delete(1.0, END)
        text_entry.delete("1.0", "end-1c")  # Deletes all entered text when click display
        text_output.insert(1.0, final_text)
        translate_click_btnInsert.configure(command=partial(translate, text))

    def insert_listbox(*args, miss_count):
        array = [*args]
        random.shuffle(array)
        words_listbox.insert(END, f'{str(miss_count)}-th missing')
        for i in array:
            words_listbox.insert(END, i)  # iadding words to the bottom of the list
        miss_count += 1

    def selected(event):  # return selected words in Listbox
        selected_indices = words_listbox.curselection()
        # get selected elements
        selected_words = " ".join([words_listbox.get(i) for i in selected_indices])
        return selected_words

    def exit_insert():  # Function to exit out of insert label
        destroy_all(text_entry, text_output, display_click_btnInsert, save_click_btnInsert,
                    right_frame, close_click_btnInsert, check_click_btnInsert, translate_click_btnInsert,
                    new_text_click_btnInsert)

    def save_in_history():  # doesn't work now
        try:
            SQL.save_in_history(text_update, datetime.now(),*user_id)
            msg = 'The text is saved'
            mb.showinfo("Saving", msg)
        except NameError:  # if user didn't display a text - show a message
            msg = 'Enter the text'
            mb.showerror("Error", msg)
            return

    def check_text():  # check the correctness of the choice
        point = 0
        array_of_mistakes = []
        global list_of_correct_words
        chosen_words = selected(event).split()
        try:
            if len(chosen_words) != len(list_of_correct_words):
                msg = f'You have chosen the wrong number of answers!'
                mb.showerror("Error", msg)
                return
        except NameError:
            msg = 'Please, enter the text'
            mb.showerror("Error", msg)
        for k, j in zip(chosen_words, list_of_correct_words):
            if k == j:
                point += 1
            else:
                array_of_mistakes.append(f'{k}, but {j} was right\n')
        if array_of_mistakes:
            msg = f'Your score is {point}/{len(list_of_correct_words)}\nYou have chosen:\n{"".join(array_of_mistakes)}'
            mb.showinfo("Info", msg)
        else:
            msg = f'Great! Your score is {point}/{len(list_of_correct_words)}'
            mb.showinfo("Info", msg)

    def new_text():
        words_listbox.delete(0, END)
        text_entry.delete("1.0", "end-1c")
        text_output.delete(1.0, END)

    text_output = Text(height=17, width=68, bg='#bec4da', wrap=WORD, font='Times')
    text_entry = Text(height=17, width=90, bg='#bec4da', wrap=WORD, font='Times')
    text_output.place(y=35, x=240)
    text_entry.place(y=435, x=240)

    right_frame = Canvas(height=326, width=155, bg='#bec4da', relief=FLAT, highlightthickness=0)
    right_frame.place(x=800, y=35)  # required method place()

    words_listbox = Listbox(right_frame, selectmode=MULTIPLE, bg='#bec4da', font='Times', relief=FLAT,
                            highlightthickness=0, height=10)
    words_listbox.pack(ipadx=1, ipady=63, anchor=CENTER)
    words_listbox.bind("<<ListboxSelect>>", selected)  # return selected words

    check_click_btnInsert = Button(text='Check', command=check_text, activebackground='grey', bd='5')
    check_click_btnInsert.place(x=330, y=385)

    display_click_btnInsert = Button(text='Display', command=partial(display, False), activebackground='grey',
                                     bd='5')
    display_click_btnInsert.place(x=250, y=385)

    close_click_btnInsert = Button(text='Close!', command=exit_insert, activebackground='grey', bd='5')
    close_click_btnInsert.place(x=750, y=385)

    save_click_btnInsert = Button(text='Save', command=save_in_history, activebackground='grey', bd='5')
    save_click_btnInsert.place(x=410, y=385)

    translate_click_btnInsert = Button(text='Translate', activebackground='grey', bd='5')
    translate_click_btnInsert.place(x=490, y=385)

    new_text_click_btnInsert = Button(text='New Text', command=new_text, activebackground='grey', bd='5')
    new_text_click_btnInsert.place(x=670, y=385)

    if from_random:
        display(random_text)


def destroy_all(*args):
    for i in args:
        i.destroy()


def handle_click_btnRandom(event):
    def handle_click_on_theme(theme):
        destroy_all(label_theme, canvas_theme, btn_random_exit)
        handle_click_btnInsert(0, True, (SQL.get_text_by_theme([theme])))

    def random_exit():
        destroy_all(btn_random_exit, canvas_theme)

    canvas_theme = Canvas(background='#d7ebf4', width=150, height=800)
    canvas_theme.place(x=200)

    label_theme = Label(canvas_theme, background='#d7ebf4', text='Themes', font=('Times', 15, tkinter.font.BOLD),
                        anchor='n')  # create add. side for different themes
    label_theme.place(x=30)
    Nature, Culture, Technology, DayofTheDate = 'Nature', 'Culture', 'Technology', 'Day of the date'  # list of topics
    btnNature = Button(canvas_theme, text=Nature, command=partial(handle_click_on_theme,
                                                                  Nature))  # when the user selects, the text on this topic will be displayed
    btnCulture = Button(canvas_theme, text=Culture, command=partial(handle_click_on_theme, Culture))
    btnTechnology = Button(canvas_theme, text=Technology, command=partial(handle_click_on_theme, Technology))
    btnDay = Button(canvas_theme, text=DayofTheDate, command=partial(handle_click_on_theme, Technology))
    btnNature.place(y=30)
    btnCulture.place(y=60)
    btnTechnology.place(y=90)
    btnDay.place(y=120)
    btn_random_exit = Button(text='Close!', command=random_exit, activebackground='grey', bd='5')
    btn_random_exit.place(x=30, y=385)


def handle_click_btnHistory(event):  # create a table with date and your previous texts

    def on_select(event):
        for i in tree.selection():
            item = tree.item(i)
            text = item['values']
            handle_click_btnInsert(event, True, text[0])
        destroy_all(tree, btn_history_exit)

    ls = SQL.return_text_from_history(user_id)

    columns = ("text", "date")

    tree = ttk.Treeview(columns=columns, show="headings", height=200)
    tree.place(x=200)

    # table's head
    tree.heading("text", text="text")
    tree.heading("date", text="date")

    tree.column("#1", stretch=YES, width=600)
    tree.column("#2", stretch=YES, width=200)

    # data
    for text in ls:
        tree.insert("", END, values=text)

    def exit_history():  # Function to exit out of insert label
        destroy_all(tree, btn_history_exit)

    tree.bind('<<TreeviewSelect>>', on_select)

    btn_history_exit = Button(text='Close!', command=exit_history, activebackground='grey', bd='5')
    btn_history_exit.place(x=30, y=385)


def handle_click_btnNewUser():  # может сделать функцию по созданию начальных виджетов? Второй раз вызываем
    def sql_new_user():
        name = entry_name.get()
        password = entry_password.get()
        if (len(name) not in range(3, 15)) or (len(password) not in range(3, 15)):
            msg = 'The length of the name and password must be no more than 15 and no less than 3 characters'
            mb.showerror("Error", msg)
        else:
            SQL.register_new_user(entry_name.get(), entry_password.get())
            msg = 'You are registered'
            mb.showinfo("Saving", msg)
            destroy_all(top_canvas, main_label, name_label, password_label, entry_password, entry_name, btnConfirm)

    top_canvas = Canvas(width=1000, height=1000, bg='#31343f', highlightthickness=0)
    top_canvas.place(width=1000, height=800)

    main_label = Label(top_canvas, bg='#31343f', text='Sign Up', font=('Times', 30, 'bold'), fg='#bec4da')
    main_label.place(y=200, x=390)

    name_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font='Times,6', text='name')
    password_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font='Times,6', text='password')
    name_label.place(y=265, x=370)
    password_label.place(y=296, x=340)

    entry_name = Entry(master=top_canvas)
    entry_password = Entry(master=top_canvas)
    entry_name.place(x=450, y=270)
    entry_password.place(x=450, y=300)

    btnBack = Button(top_canvas, fg='#bec4da', bg='#31343f', activebackground='#31343f',
                     text='Back', font='Times,4,highlight', highlightthickness=1,
                     bd=0, command=partial(handle_main_window, 1))
    btnBack.place(y=380, x=440)

    btnConfirm = Button(master=top_canvas, text='Confirm', font='Times,6', width=10, height=1, command=sql_new_user)

    btnConfirm.place(y=345, x=450)


def confirm_user(*args, name, password):
    try:
        global user_id
        user_id = SQL.confirm_user(name, password)
        destroy_all(*args)
        welcome_user = Label(fg='#bec4da', bg='#151d39', font=('Times', 16, 'bold'),
                             text='Welcome back, \n' + SQL.return_user_name(user_id), width=13)
        welcome_user.place(x=20, y=20)
    except IndexError:
        msg = 'The name or password is incorrect'
        mb.showerror("Error", msg)


def handle_main_window(event):
    top_canvas = Canvas(width=1000, height=1000, bg='#31343f', highlightthickness=0)
    top_canvas.place(width=1000, height=800)

    main_label = Label(top_canvas, bg='#31343f', text='ABC-helper', font=('Times', 30, 'bold'), fg='#bec4da')
    main_label.place(y=200, x=390)

    name_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font='Times,6', text='name')
    password_label = Label(top_canvas, fg='#bec4da', bg='#31343f', font='Times,6', text='password')
    name_label.place(y=265, x=370)
    password_label.place(y=296, x=340)

    with open('home.txt', 'r') as file:
        home_text = file.read()  # Open and read file home.txt
        home_label = Label(top_canvas, text=home_text, anchor='n', bg='#31343f', font=('Times', 15, 'bold'),
                           fg='#bec4da')
        home_label.place(x=180)

    btnNewUser = Button(top_canvas, fg='#bec4da', bg='#31343f', activebackground='#31343f',
                        text='New user here?', font='Times,4,highlight', highlightthickness=1,
                        bd=0, command=handle_click_btnNewUser)
    btnNewUser.place(y=380, x=440)

    entry_name = Entry(master=top_canvas)
    entry_password = Entry(master=top_canvas, show='*')
    entry_name.place(x=450, y=270)
    entry_password.place(x=450, y=300)

    def return_entry():
        confirm_user(entry_name, entry_password, top_canvas, main_label, name_label, password_label,
                     btnNewUser, home_label, password=entry_password.get(), name=entry_name.get())

    btnConfirm = Button(top_canvas, text='Confirm', font='Times,6', width=10, height=1,
                        command=return_entry)
    btnConfirm.place(y=345, x=450)
