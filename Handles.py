import tkinter
from tkinter import *
from Application_main import *

# class Function(Helper):
#     onClickInsert = True
#     def __init__(self, root_out, onClickInsert):
#         super().__init__(root_out)
#         self.onClickInsert = onClickInsert

def handle_click_btnInsert(event): # Create function to handle btnInsert


    # application.my_label.place(x=0, y=0, relwidth=1, relheight=1)
    def clear_main_label():
        my_label_next = Label(image = bg)
        my_label_next.place(x=0, y=0, relwidth=1, relheight=1)
        my_label.destroy()
        if hasattr(application, "my_label_next"):
            self.my_label_next.destroy()

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

    def exitInsert():
        pass

    # if Function.onClickInsert: # if the button is not pressed, the process starts
        text_label = Label() # Create window for text
        text_enter = Entry() # Create window to input text
        text_label.pack(anchor=CENTER, padx=6, pady=6)
        text_enter.pack(anchor=CENTER, padx=6, pady=6)

        # Set parameters for buttons
        display_click_btnInsert = Button(text='Display', command=display)
        display_click_btnInsert.pack(anchor=CENTER, padx=6, pady=6)

        clear_click_btnInsert = Button(text='Clear', command=clear)
        clear_click_btnInsert.pack(anchor=CENTER, padx=6, pady=6)

        # Function.onClickInsert = False

    text_label = Label(height=20,width=100,anchor = 'e') # Create window for text
    text_enter = Entry(justify= tkinter.CENTER,width=50) # Create window to input text
    text_label.pack(anchor='e', padx=49, pady=6)
    text_enter.place(anchor=CENTER, height=60,x = 580, y =400)

    



def handle_click_btnRandom(event):
    label_theme = Label( background='#d7ebf4',width=20,height=200,text='Themes',font='Bold',anchor='n',pady = 10)
    label_theme.pack()
    label_theme.place(x=200)
    create_buttons_themes()

def create_buttons_themes():
    btnNature = Button(text='Nature')
    btnSocial =Button(text = 'Social')
    btnTechnology = Button(text = 'Technology')
    btnNature.pack()
    btnSocial.pack()
    btnTechnology.pack()
    btnNature.place(x = 200,y =30)
    btnSocial.place(x = 200,y =60)
    btnTechnology.place(x = 200,y =90)

# class Home(Helper):
#     onClickHome = True
#
#     def __init__(self, root_out, onClickHome):
#         super().__init__(root_out)
#         self.onClickHome = onClickHome

def handle_click_btnHome(event): # Create function to handle btnHome
    # if Home.onClickHome: # if the button is not pressed, the process starts
        with open('home.txt', 'r') as file:
            home_text = file.read() # Open and read file home.txt
        try:
            home_label = Label(text=home_text, anchor='n')
            home_label_btn_close = Button(home_label, text='Закрыть', anchor='s', command=home_label.destroy)
            # home_label.grid(row=100, column=59)
            home_label.pack()
            home_label_btn_close.pack(padx=200, pady=100)
            # Home.onClickHome = False

        except Tk.report_callback_exception as ex:
            print('Error!', ex)

