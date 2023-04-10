# Step1: Making the screen with geometry specifics..

# from tkinter import Tk,Frame
# screen_root = Tk()

# screen_root.geometry('450x450+300+100')

# screen_root.resizable(0,0)
# screen_root.title("Calculator")
# screen_root.mainloop()

# Step2: Dividing the screen into multiple frames..

# from tkinter import Tk,Frame
# screen_root = Tk()

# screen_root.geometry('450x450+300+100')

# screen_root.resizable(0,0)
# screen_root.title("Calculator")

# frame1 = Frame(screen_root,bg='red')
# frame1.pack(fill='both',expand=True)

# frame2 = Frame(screen_root,bg='green')
# frame2.pack(fill='both',expand=True)

# frame3 = Frame(screen_root,bg='blue')
# frame3.pack(fill='both',expand=True)

# frame4 = Frame(screen_root,bg='black')
# frame4.pack(fill='both',expand=True)

# screen_root.mainloop()

# Step3 : Creating the button in the frames..

# from tkinter import Tk,Frame,Button
# screen_root = Tk()

# screen_root.geometry('450x450+300+100')

# screen_root.resizable(0,0)
# screen_root.title("Calculator")

# frame1 = Frame(screen_root,bg='red')
# frame1.pack(fill='both',expand=True)

# frame2 = Frame(screen_root,bg='green')
# frame2.pack(fill='both',expand=True)

# frame3 = Frame(screen_root,bg='blue')
# frame3.pack(fill='both',expand=True)

# frame4 = Frame(screen_root,bg='black')
# frame4.pack(fill='both',expand=True)


# btn1 = Button(frame1,text='1',font=('Verdana',20),border=0)
# btn1.pack(expand=True,fill="both",side='left')

# btn2 = Button(frame1,text='2',font=('Verdana',20),border=0)
# btn2.pack(expand=True,fill="both",side='left')

# btn3 = Button(frame1,text='3',font=('Verdana',20),border=0)
# btn3.pack(expand=True,fill="both",side='left')

# btnplus = Button(frame1,text='+',font=('Verdana',20),border=0)
# btnplus.pack(expand=True,fill="both",side='left')


# btn4 = Button(frame2,text='4',font=('Verdana',20),border=0)
# btn4.pack(expand=True,fill="both",side='left')

# btn5 = Button(frame2,text='5',font=('Verdana',20),border=0)
# btn5.pack(expand=True,fill="both",side='left')

# btn6 = Button(frame2,text='6',font=('Verdana',20),border=0)
# btn6.pack(expand=True,fill="both",side='left')

# btnminus = Button(frame2,text='-',font=('Verdana',20),border=0)
# btnminus.pack(expand=True,fill="both",side='left')

# btn7 = Button(frame3,text='7',font=('Verdana',20),border=0)
# btn7.pack(expand=True,fill="both",side='left')

# btn8 = Button(frame3,text='8',font=('Verdana',20),border=0)
# btn8.pack(expand=True,fill="both",side='left')

# btn9 = Button(frame3,text='9',font=('Verdana',20),border=0)
# btn9.pack(expand=True,fill="both",side='left')

# btnmul = Button(frame3,text='*',font=('Verdana',20),border=0)
# btnmul.pack(expand=True,fill="both",side='left')

# btnC = Button(frame4,text='C',font=('Verdana',20),border=0)
# btnC.pack(expand=True,fill="both",side='left')

# btn0 = Button(frame4,text='0',font=('Verdana',20),border=0)
# btn0.pack(expand=True,fill="both",side='left')

# btnequal = Button(frame4,text='=',font=('Verdana',20),border=0)
# btnequal.pack(expand=True,fill="both",side='left')

# btndiv = Button(frame4,text='/',font=('Verdana',20),border=0)
# btndiv.pack(expand=True,fill="both",side='left')

# screen_root.mainloop()



# Step4: Creating the Label

# from tkinter import Tk,Frame,Button,Label
# screen_root = Tk()

# screen_root.geometry('450x450+300+100')

# screen_root.resizable(0,0)
# screen_root.title("Calculator")

# label_data = Label(screen_root,text="This is Label",anchor='se',font=('Verdana',20))
# label_data.pack(expand=True,fill="both")

# frame1 = Frame(screen_root,bg='red')
# frame1.pack(fill='both',expand=True)

# frame2 = Frame(screen_root,bg='green')
# frame2.pack(fill='both',expand=True)

# frame3 = Frame(screen_root,bg='blue')
# frame3.pack(fill='both',expand=True)

# frame4 = Frame(screen_root,bg='black')
# frame4.pack(fill='both',expand=True)


# btn1 = Button(frame1,text='1',font=('Verdana',20),border=0)
# btn1.pack(expand=True,fill="both",side='left')

# btn2 = Button(frame1,text='2',font=('Verdana',20),border=0)
# btn2.pack(expand=True,fill="both",side='left')

# btn3 = Button(frame1,text='3',font=('Verdana',20),border=0)
# btn3.pack(expand=True,fill="both",side='left')

# btnplus = Button(frame1,text='+',font=('Verdana',20),border=0)
# btnplus.pack(expand=True,fill="both",side='left')


# btn4 = Button(frame2,text='4',font=('Verdana',20),border=0)
# btn4.pack(expand=True,fill="both",side='left')

# btn5 = Button(frame2,text='5',font=('Verdana',20),border=0)
# btn5.pack(expand=True,fill="both",side='left')

# btn6 = Button(frame2,text='6',font=('Verdana',20),border=0)
# btn6.pack(expand=True,fill="both",side='left')

# btnminus = Button(frame2,text='-',font=('Verdana',20),border=0)
# btnminus.pack(expand=True,fill="both",side='left')

# btn7 = Button(frame3,text='7',font=('Verdana',20),border=0)
# btn7.pack(expand=True,fill="both",side='left')

# btn8 = Button(frame3,text='8',font=('Verdana',20),border=0)
# btn8.pack(expand=True,fill="both",side='left')

# btn9 = Button(frame3,text='9',font=('Verdana',20),border=0)
# btn9.pack(expand=True,fill="both",side='left')

# btnmul = Button(frame3,text='*',font=('Verdana',20),border=0)
# btnmul.pack(expand=True,fill="both",side='left')

# btnC = Button(frame4,text='C',font=('Verdana',20),border=0)
# btnC.pack(expand=True,fill="both",side='left')

# btn0 = Button(frame4,text='0',font=('Verdana',20),border=0)
# btn0.pack(expand=True,fill="both",side='left')

# btnequal = Button(frame4,text='=',font=('Verdana',20),border=0)
# btnequal.pack(expand=True,fill="both",side='left')

# btndiv = Button(frame4,text='/',font=('Verdana',20),border=0)
# btndiv.pack(expand=True,fill="both",side='left')

# screen_root.mainloop()


# Step5 : Writing the functions for button clicked..

from tkinter import Tk,Frame,Button,Label,StringVar
screen_root = Tk()

screen_root.geometry('450x450+300+100')

screen_root.resizable(0,0)
screen_root.title("Calculator")

data = StringVar()

val = ""

def btn1_is_clicked():
    global val
    val = val+"1"
    data.set(val)

def btn2_is_clicked():
    global val
    val = val+"2"
    data.set(val)

def btn3_is_clicked():
    global val
    val = val+"3"
    data.set(val)

def btn4_is_clicked():
    global val
    val = val+"4"
    data.set(val)

def btn5_is_clicked():
    global val
    val = val+"5"
    data.set(val)

def btn6_is_clicked():
    global val
    val = val+"6"
    data.set(val)

def btn7_is_clicked():
    global val
    val = val+"7"
    data.set(val)

def btn8_is_clicked():
    global val
    val = val+"8"
    data.set(val)

def btn9_is_clicked():
    global val
    val = val+"9"
    data.set(val)

def btn0_is_clicked():
    global val
    val = val+"0"
    data.set(val)

def btnplus_is_clicked():
    global val
    val = val+"+"
    data.set(val)

def btnminus_is_clicked():
    global val
    val = val+"-"
    data.set(val)

def btnmul_is_clicked():
    global val
    val = val+"*"
    data.set(val)

def btndiv_is_clicked():
    global val
    val = val+"/"
    data.set(val)

def btnC_is_clicked():
    global val
    val = ""
    data.set(val)

def btnequal_is_clicked():
    global val
    # eval --  convert the string into the expression..
    val = eval(val)
    val = str(val)
    data.set(val)


label_data = Label(screen_root,anchor='se',font=('Verdana',20),textvariable=data)
label_data.pack(expand=True,fill="both")

frame1 = Frame(screen_root,bg='red')
frame1.pack(fill='both',expand=True)

frame2 = Frame(screen_root,bg='green')
frame2.pack(fill='both',expand=True)

frame3 = Frame(screen_root,bg='blue')
frame3.pack(fill='both',expand=True)

frame4 = Frame(screen_root,bg='black')
frame4.pack(fill='both',expand=True)


btn1 = Button(frame1,text='1',font=('Verdana',20),border=0,command=btn1_is_clicked)
btn1.pack(expand=True,fill="both",side='left')

btn2 = Button(frame1,text='2',font=('Verdana',20),border=0,command=btn2_is_clicked)
btn2.pack(expand=True,fill="both",side='left')

btn3 = Button(frame1,text='3',font=('Verdana',20),border=0,command=btn3_is_clicked)
btn3.pack(expand=True,fill="both",side='left')

btnplus = Button(frame1,text='+',font=('Verdana',20),border=0,command=btnplus_is_clicked)
btnplus.pack(expand=True,fill="both",side='left')


btn4 = Button(frame2,text='4',font=('Verdana',20),border=0,command=btn4_is_clicked)
btn4.pack(expand=True,fill="both",side='left')

btn5 = Button(frame2,text='5',font=('Verdana',20),border=0,command=btn5_is_clicked)
btn5.pack(expand=True,fill="both",side='left')

btn6 = Button(frame2,text='6',font=('Verdana',20),border=0,command=btn6_is_clicked)
btn6.pack(expand=True,fill="both",side='left')

btnminus = Button(frame2,text='-',font=('Verdana',20),border=0,command=btnminus_is_clicked)
btnminus.pack(expand=True,fill="both",side='left')

btn7 = Button(frame3,text='7',font=('Verdana',20),border=0,command=btn7_is_clicked)
btn7.pack(expand=True,fill="both",side='left')

btn8 = Button(frame3,text='8',font=('Verdana',20),border=0,command=btn8_is_clicked)
btn8.pack(expand=True,fill="both",side='left')

btn9 = Button(frame3,text='9',font=('Verdana',20),border=0,command=btn9_is_clicked)
btn9.pack(expand=True,fill="both",side='left')

btnmul = Button(frame3,text='*',font=('Verdana',20),border=0,command=btnmul_is_clicked)
btnmul.pack(expand=True,fill="both",side='left')

btnC = Button(frame4,text='C',font=('Verdana',20),border=0,command=btnC_is_clicked)
btnC.pack(expand=True,fill="both",side='left')

btn0 = Button(frame4,text='0',font=('Verdana',20),border=0,command=btn0_is_clicked)
btn0.pack(expand=True,fill="both",side='left')

btnequal = Button(frame4,text='=',font=('Verdana',20),border=0,command=btnequal_is_clicked)
btnequal.pack(expand=True,fill="both",side='left')

btndiv = Button(frame4,text='/',font=('Verdana',20),border=0,command=btndiv_is_clicked)
btndiv.pack(expand=True,fill="both",side='left')

screen_root.mainloop()