from tkinter import *

import PIL.Image
from PIL import Image, ImageTk
import Handles

class Helper:

    def __init__(self, root_out):
        self.root = root_out
        self.root.geometry("1000x800")  #define the initial area of the window
        self.root.resizable(0,0)

        # #define background image
        # self.initial_area = Label(bg='#8fbbea',width=1000,height=800)
        # self.initial_area.place()
        # self.user_name_entry = Entry()
        # self.password_entry = Entry(show='*')
        # self.btnConfirm = Button(self.initial_area, text = 'Confirm')
        # self.btnClear = Button(self.initial_area, text = 'Clear')
        # self.user_name_entry.pack()
        # self.password_entry.pack()
        # self.btnConfirm.pack()
        # self.btnClear.pack()


        self.bg = ImageTk.PhotoImage(master = self.root, file = 'pictures/background.png')
        self.leftside = ImageTk.PhotoImage(master = self.root, file = "pictures/leftside.png")

        #define title
        self.root.title("ABC-helper")

        #create main window(label)
        self.my_label = Label(master=self.root, image = self.bg)
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)   #set a coordinates of background


        self.canvas = Canvas(self.root, width=200, height=800, highlightthickness=0)  #additional area
        self.canvas.create_image(0, 0, anchor="nw", image=self.leftside)
        self.canvas.pack()        #add canvas

        self.canvas.place(x=0, y =0, width=200, height=800)          #set canvas in left side
        self.canvas.create_line(200,0,200,800,fill = '#bec4da', width=5)     #create light line


        self.btn0 = ImageTk.PhotoImage(master = self.root, file = "pictures/inserttext.png")      #open pictures for buttons

        self.btn1 = ImageTk.PhotoImage(master = self.root,file = "pictures/randomtext.png")

        self.btn2 = ImageTk.PhotoImage(master = self.root, file = "pictures/history.png")

        self.btn3 = ImageTk.PhotoImage(master = self.root,file = "pictures/home.png")

        self.btnInsert = Button(self.root, image=self.btn0, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')  #create button in object - button
        self.btnInsert.pack()             #show button
        self.btnInsert.bind('<Button-1>', handler.handle_click_btnInsert) # Run handle on click

        self.btnRandom = Button(self.root, image = self.btn1, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
        self.btnRandom.pack()
        self.btnRandom.bind('<Button-1>',Handles.handle_click_btnRandom)

        self. btnHistory = Button(self.root,image = self.btn2, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')
        self.btnHistory.pack()

        self.btnHome = Button(self.root, width = 500/3, height=200/3, image = self.btn3, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
        self.btnHome.pack()
        self.btnHome.bind('<Button-1>', home.handle_click_btnHome) # Run handle on click

        self.canvas.create_window(((200-500/3)/2-1.9,100), anchor = 'nw', window = self.btnInsert)      #set buttons on canvas
        self.canvas.create_window(((200 - 500/3)/2-1.9, 200), anchor = 'nw', window = self.btnRandom)
        self.canvas.create_window(((200 - 500/3)/2-1.9, 300), anchor = 'nw', window = self.btnHistory)
        self.canvas.create_window(((50-500/3)/2 - 1.9, 737), anchor = 'nw', window = self.btnHome)


if __name__=='__main__':
    root_out = Tk()
    application = Helper(root_out)  #class object
    handler = Handles.Function(application, False)
    home = Handles.Home(application, False)
    root_out.mainloop()  # start application