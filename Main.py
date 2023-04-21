from tkinter import *
from PIL import ImageTk

root = Tk()

root.geometry("1000x800")  #define the initial area of the window
root.resizable(0,0)

#define background image
bg = PhotoImage(file="pictures/background.png")  #open picture
leftside = PhotoImage(file = "pictures/leftside.png")

#define title
root.title("ABC-helper")

#create main window(label)
my_label = Label(root, image = bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)   #set a coordinates of background

canvas = Canvas(root, width = 200, height =800, highlightthickness=0)  #additional area
canvas.create_image(0, 0, anchor="nw", image=leftside)
canvas.pack()        #add canvas

canvas.place(x=0, y =0,width=200, height=800)          #set canvas in left side
canvas.create_line(200,0,200,800,fill = '#bec4da', width=5)     #create light line


btn0 = PhotoImage(file = "pictures/inserttext.png")      #open pictures for buttons
btn0 = btn0.subsample(3,3)                                #reduce their size

btn1 = PhotoImage(file = "pictures/randomtext.png")
btn1 = btn1.subsample(3,3)

btn2 = PhotoImage(file = "pictures/history.png")
btn2 = btn2.subsample(3,3)

btn3 = PhotoImage(file = "pictures/home.png")



btnInsert = Button(root, image=btn0, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')  #create button in object - button
btnInsert.pack()             #show button

btnRandom = Button(root, image = btn1, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
btnRandom.pack()

btnHistory = Button(root,image = btn2, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')
btnHistory.pack()

btnHome = Button(root,width = 500/3, height=200/3, image = btn3, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
btnHome.pack()

canvas.create_window(((200-500/3)/2-1.9,100), anchor = 'nw', window = btnInsert)      #set buttons on canvas
canvas.create_window(((200 - 500/3)/2-1.9, 200), anchor = 'nw', window = btnRandom)
canvas.create_window(((200 - 500/3)/2-1.9, 300), anchor = 'nw', window = btnHistory)
canvas.create_window(((50-500/3)/2 - 1.9, 737), anchor = 'nw', window = btnHome)


root.mainloop()                         # start application

