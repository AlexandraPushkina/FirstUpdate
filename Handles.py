from tkinter import *
from Main import *

class Function(Helper):
    onClickInsert = True
    def __init__(self, root_out, onClickInsert):
        super().__init__(root_out)
        self.onClickInsert = onClickInsert


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

        def exitInsert():
            pass

        if Function.onClickInsert: # if the button is not pressed, the process starts 
            text_label = Label() # Create window for text 
            text_enter = Entry() # Create window to input text
            text_label.pack(anchor=CENTER, padx=6, pady=6)
            text_enter.pack(anchor=CENTER, padx=6, pady=6)
                        
            # Set parameters for buttons
            display_click_btnInsert = Button(text='Display', command=display)
            display_click_btnInsert.pack(anchor=CENTER, padx=6, pady=6)

            clear_click_btnInsert = Button(text='Clear', command=clear)
            clear_click_btnInsert.pack(anchor=CENTER, padx=6, pady=6)
            
            Function.onClickInsert = False

    

class Home(Helper):
    onClickHome = True
    def __init__(self, root_out, onClickHome):
        super().__init__(root_out)
        self.onClickHome = onClickHome

    
    def handle_click_btnHome(event): # Create function to handle btnHome
        # canvas.delete()                   # You must delete canvas
        
        if Home.onClickHome: # if the button is not pressed, the process starts
            with open('home.txt', 'r') as file:
                home_text = file.read() # Open and read file home.txt
            try:
                home_label = Label(text=home_text, anchor='n')
                home_label_btn_close = Button(home_label, text='Закрыть', anchor='s', command=home_label.destroy)
                # home_label.grid(row=100, column=59)
                home_label.pack()
                home_label_btn_close.pack(padx=200, pady=100)
                Home.onClickHome = False
                    
            except Tk.report_callback_exception as ex:
                print('Error!', ex)

