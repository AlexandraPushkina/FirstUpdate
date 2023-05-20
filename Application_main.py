from tkinter import *
# from PIL import ImageTk
from Handles import handle_click_btnInsert, handle_click_btnRandom, handle_click_btnHome

class Helper:

    def __init__(self, root_out):
        self.root = root_out
        self.root.geometry("1000x800")  #define the initial area of the window
        self.root.resizable(0,0)

        #define background image
        self.bg = PhotoImage(file="pictures/background.png")  #open picture
        self.leftside = PhotoImage(file = "pictures/leftside.png")

        #define title
        self.root.title("ABC-helper")

        #create main window(label)
        self.my_label = Label(self.root, image = self.bg)
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)   #set a coordinates of background


        self.canvas = Canvas(self.root, width=200, height=800, highlightthickness=0)  #additional area
        self.canvas.create_image(0, 0, anchor="nw", image=self.leftside)
        self.canvas.pack()        #add canvas

        self.canvas.place(x=0, y =0,width=200, height=800)          #set canvas in left side
        self.canvas.create_line(200,0,200,800,fill = '#bec4da', width=5)     #create light line


        self.btn0 = PhotoImage(file = "pictures/inserttext.png")      #open pictures for buttons
        self.btn0 = self.btn0.subsample(3,3)                                #reduce their size

        self.btn1 = PhotoImage(file = "pictures/randomtext.png")
        self.btn1 = self.btn1.subsample(3,3)

        self.btn2 = PhotoImage(file = "pictures/history.png")
        self.btn2 = self.btn2.subsample(3,3)

        self.btn3 = PhotoImage(file = "pictures/home.png")

        self.btnInsert = Button(self.root, image=self.btn0, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')  #create button in object - button
        self.btnInsert.pack()             #show button
        self.btnInsert.bind('<Button-1>', handle_click_btnInsert) # Run handle on click

        self.btnRandom = Button(self.root, image = self.btn1, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
        self.btnRandom.pack()
        self.btnRandom.bind('<Button-1>', handle_click_btnRandom)

        self. btnHistory = Button(self.root,image = self.btn2, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')
        self.btnHistory.pack()

        self.btnHome = Button(self.root,width = 500/3, height=200/3, image = self.btn3, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
        self.btnHome.pack()
        self.btnHome.bind('<Button-1>', handle_click_btnHome) # Run handle on click

        self.canvas.create_window(((200-500/3)/2-1.9,100), anchor = 'nw', window = self.btnInsert)      #set buttons on canvas
        self.canvas.create_window(((200 - 500/3)/2-1.9, 200), anchor = 'nw', window = self.btnRandom)
        self.canvas.create_window(((200 - 500/3)/2-1.9, 300), anchor = 'nw', window = self.btnHistory)
        self.canvas.create_window(((50-500/3)/2 - 1.9, 737), anchor = 'nw', window = self.btnHome)


if __name__=='__main__':
    root_out = Tk()
    application = Helper(root_out)  #class object
    root_out.mainloop()  # start application