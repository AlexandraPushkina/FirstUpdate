from tkinter import *
from PIL import Image, ImageTk
from Handles import *

if __name__=='__main__':
    root = Tk()

    root.geometry("1000x800")  #define the initial area of the window
    root.resizable(0,0)
    # root.grid_columnconfigure(0,minsize=199)
    # root.grid_columnconfigure(1,minsize=810)


    bg = ImageTk.PhotoImage(master =root, file = 'pictures/background.png')
    leftside = ImageTk.PhotoImage(master = root, file = "pictures/leftside.png")

    #define title
    root.title("ABC-helper")

    #create main window(label)
    my_label = Label(master=root, image = bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)   #set a coordinates of background

    canvas = Canvas(root, width=200, height=800, highlightthickness=0)  #additional area
    canvas.create_image(0, 0, anchor="nw", image=leftside)
    canvas.pack()        #add canvas

    canvas.place(x=0, y =0, width=200, height=800)          #set canvas in left side
    canvas.create_line(200,0,200,800,fill = '#bec4da', width=5)     #create light line


    btn0 = ImageTk.PhotoImage(master = root, file = "pictures/inserttext.png")      #open pictures for buttons

    btn1 = ImageTk.PhotoImage(master = root,file = "pictures/randomtext.png")

    btn2 = ImageTk.PhotoImage(master = root, file = "pictures/history.png")

    btn3 = ImageTk.PhotoImage(master =root,file = "pictures/home.png")


    btnInsert = Button(root, image=btn0, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')  #create button in object - button
    btnInsert.pack()             #show button
    btnInsert.bind('<Button-1>',handle_click_btnInsert) # Run handle on click

    btnRandom = Button(root, image = btn1, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
    btnRandom.pack()
    btnRandom.bind('<Button-1>',handle_click_btnRandom)

    btnHistory = Button(root,image =btn2, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39')
    btnHistory.pack()
    btnHistory.bind('<Button-1>', handle_click_btnHistory)

    btnHome = Button(root, width = 500/3, height=200/3, image = btn3, highlightthickness=1,bd = 0,activebackground='#151d39', background='#151d39' )
    btnHome.pack()
    btnHome.bind('<Button-4>', handle_click_btnHome) # Run handle on click

    canvas.create_window(((200-500/3)/2-1.9,100), anchor = 'nw', window = btnInsert)      #set buttons on canvas
    canvas.create_window(((200 - 500/3)/2-1.9, 200), anchor = 'nw', window = btnRandom)
    canvas.create_window(((200 - 500/3)/2-1.9, 300), anchor = 'nw', window = btnHistory)
    canvas.create_window(((50-500/3)/2 - 1.9, 737), anchor = 'nw', window = btnHome)

    top_canvas =Canvas(root,width=1000, height=1000,bg='#31343f',highlightthickness=0)
    top_canvas.place(width=1000, height=800)

    welcome_label = Label(top_canvas, bg='#31343f',text = 'ABC-helper',font=('Times',30,'bold'),fg = '#bec4da')
    welcome_label.place(y=200,x = 390)

    name_label = Label(top_canvas,fg ='#bec4da',bg = '#31343f',font=('Times,6'),text = 'name')
    password_label = Label(top_canvas,fg ='#bec4da',bg = '#31343f',font=('Times,6'),text = 'password' )
    name_label.place(y=265,x = 370)
    password_label.place(y=296 , x=340)

    btnNewUser = Button(top_canvas,fg ='#bec4da',bg='#31343f',activebackground='#31343f',
                        text = 'New user here?',font=('Times,4,highlight'),highlightthickness=1,
                        bd = 0,command=handle_click_btnNewUser)
    btnNewUser.place(y=380,x=440)

    entry_name = Entry(master=top_canvas)
    entry_password = Entry(master=top_canvas,show='*')
    entry_name.place(x=450,y=270)
    entry_password.place(x=450,y=300)

    def return_entry():
        confirm_user(entry_name.get(),entry_password.get(),top_canvas,welcome_label,name_label,password_label,btnNewUser,entry_password,entry_name)

    btnConfirm = Button(top_canvas, text='Confirm', font=('Times,6'), width=10, height=1,
                        command=return_entry)
    btnConfirm.place(y=345, x=450)
    # btnConfirm.bind('<Button-1>', handle_click_btnConfirm)



    root.mainloop()  # start application
