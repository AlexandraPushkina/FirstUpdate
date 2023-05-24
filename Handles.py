from tkinter import *
import Application_main
from tkinter import ttk
import tkinter.messagebox as mb
import SQL
from datetime import datetime
from functools import partial

def handle_click_btnInsert(event): # Create function to handle btnInsert

    def clear(): # function to remove a character in the entered text
         Text.delete(text_text, 0)

    def display(): # Function to display changed text
        global text_update
        text_update = ''
        text = text_text.get("1.0","end-1c")
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(len(text)):
            if text[i] in num_list:
                text_update += '1,2,3'
            else:
                text_update += text[i]

        # text_label['text'] = text_update
        text_text.delete("1.0","end-1c")  # Deletes all entered text when click display



    def exit_insert():  # Function to exit out of insert label
        text_label.destroy()
        # text_enter.destroy()
        display_click_btnInsert.destroy()
        clear_click_btnInsert.destroy()
        btn_insert_exit.destroy()
        global click_btn_insert
        click_btn_insert = False

    def save_in_history():
        try:
            SQL.save_in_history(text_update,datetime.now() )
            print(datetime.now())
            msg = 'Текст сохранен'
            mb.showinfo("Сохранение", msg)
        except NameError :           #if user didn't display a text - show a message
            msg = 'Введите текст'
            mb.showerror("Ошибка", msg)
            return 0

    global click_btn_insert
    # Set parameters for buttons
    click_btn_insert = False
    if not click_btn_insert:
        text_label = Label(height=20,width=100,anchor = 'e') # Create window for text
        # text_enter = Entry(justify= CENTER,width=50) # Create window to input text
        text_text = Text(height=20,width=88)

        # text_enter.delete(0, END)
        text_label.pack(anchor='e', padx=49, pady=6)
        # text_enter.place(anchor=CENTER, height=60,x = 580, y =400)
        text_text.pack(anchor='e', padx=49, pady=60)

        display_click_btnInsert = Button(text='Display', command=display)
        display_click_btnInsert.place(x = 300,y = 500)

        clear_click_btnInsert = Button(text='Clear', command=clear)
        clear_click_btnInsert.place(x = 300,y = 450)

        btn_insert_exit = Button(text='Закрыть', command=exit_insert)
        btn_insert_exit.place(x = 300,y = 400)

        btn_insert_exit = Button(text='Сохранить', command=save_in_history)
        btn_insert_exit.place(x=300, y=350)

        click_btn_insert = True



def handle_click_btnRandom(event):
    def handle_click_on_theme(theme):
        label_theme.destroy() #after clicking on theme, left board will be deleted
        btnNature.destroy()
        btnSocial.destroy()
        btnTechnology.destroy()
        text_label = Label(height=20, width=100, anchor='e')
        text_label.pack(anchor='e', padx=49, pady=6)
        text_label['text'] = SQL.get_text_by_theme(theme)


    label_theme = Label( background='#d7ebf4',width=20,height=200,text='Themes',font='Bold',anchor='n',pady = 10)  # create add. side for different themes
    label_theme.pack()
    label_theme.place(x=200)
    Nature, Social,Technology = 'Nature','Social','Technology'  #list of topics
    btnNature = Button(text=Nature,command=partial(handle_click_on_theme, Nature))   #when the user selects, the text on this topic will be displayed
    btnSocial = Button(text = Social, command=partial(handle_click_on_theme, Social))
    btnTechnology = Button(text = Technology, command=partial(handle_click_on_theme,Social))
    btnNature.pack()
    btnSocial.pack()
    btnTechnology.pack()
    btnNature.place(x = 200,y =30)
    btnSocial.place(x = 200,y =60)
    btnTechnology.place(x = 200,y =90)


def handle_click_btnHome(event): # Create function to handle btnHome
    with open('home.txt', 'r') as file:
        home_text = file.read() # Open and read file home.txt
    try:
        home_label = Label(text=home_text, anchor='n')
        home_label_btn_close = Button(home_label, text='Закрыть', anchor='s', command=home_label.destroy)
        # home_label.grid(row=100, column=59)
        home_label.pack()
        home_label_btn_close.pack(padx=200, pady=100)

    except Tk.report_callback_exception as ex:
        print('Error!', ex)

def handle_click_btnHistory(event):  #create a table with date and your previos texts
    # data
    ls = SQL.return_text_for_history()
    print(ls)

    columns = ("text", "date")

    tree = ttk.Treeview(columns=columns, show="headings",height=200)
    # tree.grid(sticky = 'we',column=1,row=1)
    tree.pack(side= RIGHT)

    # table's head
    tree.heading("text", text="text")
    tree.heading("date", text="date")

    tree.column("#1", stretch=YES, width=600)
    tree.column("#2", stretch=YES, width=200)

    # data
    for text in ls:
        tree.insert("", END, values=text)
