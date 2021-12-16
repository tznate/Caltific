from tkinter import*
import tkinter as tk
from tkinter import ttk
import math 
from math import sin,cos,tan,pi,log
from tkinter import messagebox
from tkinter.font import BOLD
from typing import Sized
from PIL import Image
import time
import os 
import webbrowser

root = Tk()
root.geometry("288x450+400+170")
root.configure(background="black") 
root.overrideredirect(True)
frameCnt = 28
frames = [PhotoImage(file='GIF\loads.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame, bg="black")
    root.after(50, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)

name = PhotoImage(file = r"images\name.png")
nameimage = name.subsample(1,1)
panel = Label(root, image = name)
panel.pack(side = "bottom", fill = "both", expand = "yes")



def main_window():
    root.destroy()
    window = Tk()
    screenSize = "288x450+400+170"
    window.geometry(screenSize)
    window.resizable(0,0)
    window.title("Caltific")

    global text_editor_mat
    global text_editor_sci

    def add_mat_formula(event):
        global text_editor_mat
        content = str(text_editor_mat.get(1.0, END))
        with open('Math.txt','w',encoding='utf-8') as fw:
            fw.write(content)

    def add_sci_formula(event):
        global text_editor_sci
        content = str(text_editor_sci.get(1.0, END))
        with open('Sci.txt','w',encoding='utf-8') as fw:
            fw.write(content)


    def about():
        messagebox.showinfo('About',"\n \n \n   Made by The Boys(Nathan, Varad)  \n\n")

    def clickButton(item):
        global expression
        inputText.set(inputText.get()+(str(item)))

    def clearButton():
        global expression
        expression = ""
        inputText.set(inputText.get()[0:-1])

    def clearAll():
        inputText.set("")

    def expand():
        if screenSize=="288x450":
            window.geometry("288x600")
        else:
            window.geometry("288x600")

    def reduce():
        if screenSize=="288x600":
            window.geometry("288x450")
        else:
            window.geometry("288x450")
    
    def equalButton():
        result = ""
        try:
            result = eval(inputText.get())
            inputText.set(result)
        except:
            result = "ERROR..."
            inputText.set(result)

    
    
    scicalci=ttk.Notebook(window)

    calc = Frame(scicalci)
    form= Frame(scicalci)
    sum = Frame(scicalci)

    scicalci.add(calc, text="Calculator")
    scicalci.add(form, text="Notes")
    scicalci.add(sum, text="Problems")
    scicalci.pack()
    window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='images/caltific.png'))

    # filemenu = Menu(menubar, tearoff=0,bg="black",fg="white")
    # filemenu.add_command(label="Copy")
    # filemenu.add_command(label="Paste")
    # filemenu.add_separator()
    # filemenu.add_command(label="Exit", command=window.quit)
    # menubar.add_cascade(label="Edit", menu=filemenu)
    # helpmenu = Menu(menubar, tearoff=0,bg="black",fg="white")
    # helpmenu.add_command(label="About", command=about)
    # menubar.add_cascade(label="Help", menu=helpmenu)

    
    inputText = StringVar()
    

    inputFrame = Frame(calc, width=312, height=55, bd=0, highlightbackground="black", highlightcolor="black",
                        highlightthickness=2,borderwidth=0)
    inputFrame.pack(side=TOP)
    inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50,fg="white", bg="black", bd=0,
                        justify=RIGHT)
    inputField.grid(row=0, column=0)
    inputField.pack(ipady=13)

    mainFrame = Frame(calc, width=312, height=272.5, bg="black", borderwidth=0)
    mainFrame.pack()

    ac = PhotoImage(file = r"images\ac.png")
    acimage = ac.subsample(2,2)
    ac = Button(mainFrame, text="AC", fg="black", image=acimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clearAll()).grid(row=0, column=0, padx=1, pady=1)

    clear = PhotoImage(file = r"images\clear.png")
    clearimage = clear.subsample(2,2)
    clear = Button(mainFrame, text="AC", fg="black", image=clearimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clearButton()).grid(row=0, column=1, padx=1, pady=1)


    expan_btn = PhotoImage(file = r"images\expan_btn.png")
    expan_btnimage = expan_btn.subsample(2,2)
    expan_btn = Button(mainFrame, fg="black", image=expan_btnimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("^")).grid(row=0, column=2, padx=1, pady=1)

    divide = PhotoImage(file = r"images\divide.png")
    divideimage = divide.subsample(2,2)
    divide = Button(mainFrame, text="/", fg="white",image=divideimage, bd=0, bg="black", cursor="hand2",
                    command=lambda: clickButton("/")).grid(row=0, column=3, padx=1, pady=1)


    seven = PhotoImage(file = r"images\seven.png")
    sevenimage = seven.subsample(2,2)
    seven = Button(mainFrame, text="7", fg="black", image=sevenimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(7)).grid(row=1, column=0, padx=1, pady=1)

    eight = PhotoImage(file = r"images\eight.png")
    eightimage = eight.subsample(2,2)
    eight = Button(mainFrame, text="8", fg="black", image=eightimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(8)).grid(row=1, column=1, padx=1, pady=1)

    nine = PhotoImage(file = r"images\nine.png")
    nineimage = nine.subsample(2,2)
    nine = Button(mainFrame, text="9", fg="black", image=nineimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(9)).grid(row=1, column=2, padx=1, pady=1)

    multi = PhotoImage(file = r"images\multi.png")
    multiimage = multi.subsample(2,2)
    multi = Button(mainFrame, text="*", fg="white",image=multiimage, bd=0, bg="black", cursor="hand2",
                    command=lambda: clickButton("*")).grid(row=1, column=3, padx=1, pady=1)

    four = PhotoImage(file = r"images\four.png")
    fourimage = four.subsample(2,2)
    four = Button(mainFrame, text="4", fg="black", image=fourimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(4)).grid(row=2, column=0, padx=1, pady=1)

    five = PhotoImage(file = r"images\five.png")
    fiveimage = five.subsample(2,2)
    five = Button(mainFrame, text="5", fg="black", image=fiveimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(5)).grid(row=2, column=1, padx=1, pady=1)

    six = PhotoImage(file = r"images\six.png")
    siximage = six.subsample(2,2)
    six = Button(mainFrame, text="6", fg="black", image=siximage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(6)).grid(row=2, column=2, padx=1, pady=1)

    minus = PhotoImage(file = r"images\minus.png")
    minusimage = minus.subsample(2,2)
    minus = Button(mainFrame, text="-", fg="white",image=minusimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("-")).grid(row=2, column=3, padx=1, pady=1)

    one = PhotoImage(file = r"images\one.png")
    oneimage = one.subsample(2,2)
    one = Button(mainFrame, text="1", fg="black", image=oneimage,bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(1)).grid(row=3, column=0, padx=1, pady=1)

    two = PhotoImage(file = r"images\two.png")
    twoimage = two.subsample(2,2)
    two = Button(mainFrame, text="2", fg="black",image=twoimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(2)).grid(row=3, column=1, padx=1, pady=1)

    three = PhotoImage(file = r"images\three.png")
    threeimage = three.subsample(2,2)
    three = Button(mainFrame, text="3", fg="black",image=threeimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(3)).grid(row=3, column=2, padx=1, pady=1)

    plus = PhotoImage(file = r"images\plus.png")
    plusimage = plus.subsample(2,2)
    plus = Button(mainFrame, text="+", fg="white",image=plusimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("+")).grid(row=3, column=3, padx=1, pady=1)


    zero = PhotoImage(file = r"images\0.png")
    zeroimage = zero.subsample(2,2)
    zero = Button(mainFrame, text="0", fg="black",image=zeroimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

    point = PhotoImage(file = r"images\point.png")
    pointimage = point.subsample(2,2)
    point = Button(mainFrame, text=".", fg="black",image=pointimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(".")).grid(row=4, column=2, padx=1, pady=1)


    equal = PhotoImage(file = r"images\equal.png")
    equalimage = equal.subsample(2,2)
    equal = Button(mainFrame, text="=", image=equalimage, fg="white", bd=0, bg="black", cursor="hand2",
                    command=lambda: equalButton()).grid(row=4, column=3, padx=1, pady=1)

    expan = PhotoImage(file = r"images\expand.png")
    expanimage = expan.subsample(1,2)
    expan = Button(mainFrame, text="=", image=expanimage, fg="white", bd=0, bg="black", cursor="hand2",
                    command=lambda: expand()).grid(row=5, column=0,columnspan=5, padx=1, pady=1)

    bracket1 = PhotoImage(file = r"images\bracket1.png")
    bracket1image = bracket1.subsample(2,2)
    bracket1 = Button(mainFrame, text="pi", fg="black",image=bracket1image, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("(")).grid(row=6, column=0, padx=1, pady=1)

    bracket2 = PhotoImage(file = r"images\bracket2.png")
    bracket2image = bracket2.subsample(2,2)
    bracket2 = Button(mainFrame, text="pi", fg="black",image=bracket2image, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton(")")).grid(row=6, column=1, padx=1, pady=1)



    π = 3.1415
    pi = PhotoImage(file = r"images\pi.png")
    piimage = pi.subsample(2,2)
    pi = Button(mainFrame, text="pi", fg="black",image=piimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("π")).grid(row=6, column=2, padx=1, pady=1)

    e = 2.7182
    ee = PhotoImage(file = r"images\eie.png")
    eeimage = ee.subsample(2,2)
    ee = Button(mainFrame, text="pi", fg="black",image=eeimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("e")).grid(row=6, column=3, padx=1, pady=1)

    sin_btn = PhotoImage(file = r"images\sin_btn.png")
    sin_btnimage = sin_btn.subsample(2,2)
    sin_btn = Button(mainFrame, text=sin, fg="black",image=sin_btnimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("sin(")).grid(row=7, column=0, padx=1, pady=1)

    cos_btn = PhotoImage(file = r"images\cos_btn.png")
    cos_btnimage = cos_btn.subsample(2,2)
    cos_btn = Button(mainFrame, text=cos, fg="black",image=cos_btnimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("cos(")).grid(row=7, column=1, padx=1, pady=1)

    tan_btn = PhotoImage(file = r"images\tan_btn.png")
    tan_btnimage = tan_btn.subsample(2,2)
    tan_btn = Button(mainFrame, text=tan, fg="black",image=tan_btnimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("tan(")).grid(row=7, column=2, padx=1, pady=1)

    log_btn = PhotoImage(file = r"images\log_btn.png")
    log_btnimage = log_btn.subsample(2,2)
    log_btn = Button(mainFrame, text=log, fg="black",image=log_btnimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("log(")).grid(row=7, column=3, padx=1, pady=1)

    redu = PhotoImage(file = r"images\reduce.png")
    reduimage = redu.subsample(1,2)
    redu = Button(mainFrame, text="=", image=reduimage, fg="white", bd=0, bg="black", cursor="hand2",
                    command=lambda: reduce()).grid(row=8, column=0,columnspan=5, padx=1, pady=1)
    #varad
    subjects=ttk.Notebook(form)

    sci= Frame(subjects)
    mat= Frame(subjects)
    
    subjects.add(sci, text="Science")
    subjects.add(mat, text="Maths")

    subjects.pack()

    sci.configure(bg="black")
    mat.configure(bg="black")


    status_bar_sci=ttk.Frame(sci,height=50)
    status_bar_sci.pack(side=BOTTOM,fill=BOTH)
    afs_btn = PhotoImage(file = r"images\af.png")
    afsimage = afs_btn.subsample(1,1)
    afs_btn = Button(sci, text="Add Formula",fg="black", image=afsimage, bd=0, bg="black", cursor="hand2")
    afs_btn.place(relx=0.5, rely=0.95, anchor=CENTER)
    afs_btn.bind('<Button>', add_sci_formula)

    text_editor_sci=Text(sci,undo=True)
    text_editor_sci.config(wrap='word', relief=FLAT)

    scroll_bar=Scrollbar(sci)
    text_editor_sci.focus_set()
    scroll_bar.pack(side=RIGHT, fill=Y)
    text_editor_sci.grid_columnconfigure(0, weight=1)
    text_editor_sci.pack(fill=BOTH,expand=True)
    scroll_bar.config(command=text_editor_sci.yview)
    text_editor_sci.config(yscrollcommand=scroll_bar.set,height=665)
    text_editor_sci.config(wrap='word', relief=FLAT)

    with open('Sci.txt','r') as fr:
        text_editor_sci.delete(1.0,END)
        text_editor_sci.insert(1.0,fr.read())

    status_bar_mat=ttk.Frame(mat,height=50)
    status_bar_mat.pack(side=BOTTOM,fill=BOTH)  
    afm_btn = PhotoImage(file = r"images\af.png")
    afmimage = afm_btn.subsample(1,1)
    afm_btn = Button(mat, text="Add Formula", image=afmimage, bd=0, bg="black", cursor="hand2")
    afm_btn.place(relx=0.5, rely=0.95, anchor=CENTER)
    afm_btn.bind('<Button>', add_mat_formula)

    text_editor_mat=Text(mat,undo=True)
    text_editor_mat.config(wrap='word', relief=FLAT)

    scroll_bar=Scrollbar(mat)
    text_editor_mat.focus_set()
    scroll_bar.pack(side=RIGHT, fill=Y)
    text_editor_mat.pack(fill=BOTH,expand=True)
    scroll_bar.config(command=text_editor_mat.yview)
    text_editor_mat.config(yscrollcommand=scroll_bar.set,height=665)
    text_editor_mat.config(wrap='word', relief=FLAT)

    with open('Math.txt','r') as fr:
        text_editor_mat.delete(1.0,END)
        text_editor_mat.insert(1.0,fr.read())


    sub=ttk.Notebook(sum)
    sum.configure(background="black")

    sci_sum= Frame(sub,width=580,height=665)
    sci_sum.pack(fill=BOTH,expand=True)
    mat_sum= Frame(sub)

    sub.add(sci_sum, text="Science")
    sub.add(mat_sum, text="Maths")

    sub.pack()

    mat_sum.configure(bg='black')
    sci_sum.configure(bg='black')
    def indices(event=None):
        main = Toplevel()
        main.title("Caltific")
        main.resizable(width=False, height=False)
        main.geometry("288x450+690+170")
        main.tk.call('wm', 'iconphoto', main._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(main,text="Chapter : Indices",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=60,y=6)
        main.configure(bg='black')

        def power(event):
            n=name_var1.get()
            x=name_var2.get()
            ans=x**n
            ansbx1.delete(0,END)
            ansbx1.insert(0,str(ans))

        def root(event):
            n=name_var3.get()
            x=name_var4.get()
            ans=x**(1/n)
            ansbx2.delete(0,END)
            ansbx2.insert(0,str(ans))


        topic1=ttk.Label(main,text="1) Final Value",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=34)
        name_label2=ttk.Label(main,text="Enter the nth root : ",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=54)
        name_var1=IntVar()
        etrybx1=ttk.Entry(main,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=57)
        name_label3=ttk.Label(main,text="Enter the variable : ",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=75)
        name_var2=IntVar()
        etrybx2=ttk.Entry(main,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=77)
        btn1=Button(main,text="Calculate")
        btn1.place(x=45,y=97)
        btn1.bind('<Button>',power)
        ansbx1=ttk.Entry(main,width=16)
        ansbx1.place(x=130,y=100)
       

        topic2=ttk.Label(main,text="2) nth value (n=power)",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=10,y=150)
        name_label4=ttk.Label(main,text="Enter the nth root : ",foreground="#FF8A00",background="black")
        name_label4.place(x=25,y=170)
        name_var3=IntVar()
        etrybx2=ttk.Entry(main,width=16,textvariable=name_var3)
        etrybx2.place(x=130,y=173)
        name_label5=ttk.Label(main,text="Enter the variable : ",foreground="#FF8A00",background="black")
        name_label5.place(x=25,y=191)
        name_var4=IntVar()
        etrybx3=ttk.Entry(main,width=16,textvariable=name_var4)
        etrybx3.place(x=130,y=193)
        btn2=Button(main,text="Calculate")
        btn2.place(x=45,y=213)
        btn2.bind("<Button>",root)
        ansbx2=ttk.Entry(main,width=16)
        ansbx2.place(x=130,y=216)
        name_label21=ttk.Label(main,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label21.place(x=10,y=255)
        
        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(main,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.place(x=90,y=420)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/vLSkRi5_HKQ"))
        
        c11 = PhotoImage(file = "./chapter/indices1.png")
        c11image = c11.subsample(5,5)
        w11 = Label(main, image=c11image)
        w11.place(x=15,y=275)

        c25 = PhotoImage(file = r"chapter/indices2.png")
        c25image = c25.subsample(2,2)
        w25 = Label(main, image=c25image)
        w25.place(x=19,y=0)

        

    def expansion(event=None):
        window1 = Toplevel()
        window1.title("Caltific")
        window1.resizable(width=False, height=False)
        window1.geometry("580x675+340+11")
        window1.configure(bg='black')
        window1.tk.call('wm', 'iconphoto', window1._w, PhotoImage(file='images/caltific.png'))



        name_label1=ttk.Label(window1,text="Chapter : Expansion Formula",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=150,y=6)

        def expansionOne(event):
            a=int(name_var1.get())
            b=int(name_var2.get())
            ansbx1.delete(0,END)
            ansbx1.insert(0,str("x² + ("+str(a+b)+"x) + ("+str(a*b)+")"))

        def expansionTwo(event):
            a=name_var3.get()
            b=name_var4.get()
            c=name_var5.get()
            sqra=""
            digits=[]
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqra+=str(char+"²")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                sqra=str(int(ans)**2)+sqra

            sqrb=""
            ans=""
            digits=[]
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrb+=str(char+"²")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                sqrb=str(int(ans)**2)+sqrb

            sqrc=""
            ans=""
            digits=[]
            for char in c:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrc+=str(char+"²")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                sqrc=str(int(ans)**2)+sqrc

            ab=""
            ans_ab=2
            ans=""
            digits=[]
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    ab+=char
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_ab*=int(ans)

            ans=""
            digits=[]
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    ab+=char
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_ab*=int(ans)
            ab=str(ans_ab)+ab

            bc=""
            ans_bc=2
            ans=""
            digits=[]
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    bc+=char
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_bc*=int(ans)

            ans=""
            digits=[]
            for char in c:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    bc+=char
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_bc*=int(ans)
            bc=str(ans_bc)+bc

            ac=""
            ans_ac=2
            ans=""
            digits=[]
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    ac+=char
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_ac*=int(ans)

            ans=""
            digits=[]
            for char in c:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    ac+=char
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_ac*=int(ans)
            ac=str(ans_ac)+ac

            ansbx2.delete(0,END)
            ansbx2.insert(0,str(str(sqra)+" + "+str(sqrb)+" + "+str(sqrc)+" + ("+str(ab)+") + ("+str(bc)+") + ("+str(ac)+")"))

        def expansionThree(event):
            a=name_var6.get()
            b=name_var7.get()
            sqra=""
            digits=[]
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqra+=str(char+"²")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                sqra=str(int(ans)**2)+sqra

            sqrb=""
            ans=""
            digits=[]
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrb+=str(char+"²")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                sqrb=str(int(ans)**2)+sqrb
            
            cbua=""
            ans=""
            digits=[]
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    cbua+=str(char+"³")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                cbua=str(int(ans)**3)+cbua

            cbub=""
            ans=""
            digits=[]
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    cbub+=str(char+"³")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                cbub=str(int(ans)**3)+cbub
            
            sqrab=""
            ans_sqrab=3
            digits=[]
            for char in sqra:
                if char in ['²','³']:
                    sqrab+=str(char)
                elif char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrab+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrab=ans_sqrab*int(ans)
            digits=[]
            ans=""
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrab+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrab=ans_sqrab*int(ans)
            digits=[]
            sqrab=str(ans_sqrab)+sqrab

            sqrba=""
            ans_sqrba=3
            digits=[]
            for char in sqrb:
                if char in ['²','³']:
                    sqrba+=str(char)
                elif char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrba+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrba=ans_sqrba*int(ans)
            digits=[]
            ans=""
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrba+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrba=ans_sqrba*int(ans)
            digits=[]
            sqrba=str(ans_sqrba)+sqrba

            ansbx3.delete(0,END)
            ansbx3.insert(0,str(str(cbua)+" + "+str(sqrab)+" + "+str(sqrba)+" + "+str(cbub)))

        def expansionFour(event):
            a=name_var8.get()
            b=name_var9.get()
            sqra=""
            digits=[]
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqra+=str(char+"²")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                sqra=str(int(ans)**2)+sqra

            sqrb=""
            ans=""
            digits=[]
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrb+=str(char+"²")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                sqrb=str(int(ans)**2)+sqrb
            
            cbua=""
            ans=""
            digits=[]
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    cbua+=str(char+"³")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                cbua=str(int(ans)**3)+cbua

            cbub=""
            ans=""
            digits=[]
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    cbub+=str(char+"³")
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                cbub=str(int(ans)**3)+cbub
            
            sqrab=""
            ans_sqrab=3
            digits=[]
            for char in sqra:
                if char in ['²','³']:
                    sqrab+=str(char)
                elif char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrab+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrab=ans_sqrab*int(ans)
            digits=[]
            ans=""
            for char in b:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrab+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrab=ans_sqrab*int(ans)
            digits=[]
            sqrab=str(ans_sqrab)+sqrab

            sqrba=""
            ans_sqrba=3
            digits=[]
            for char in sqrb:
                if char in ['²','³']:
                    sqrba+=str(char)
                elif char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrba+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrba=ans_sqrba*int(ans)
            digits=[]
            ans=""
            for char in a:
                if char in ['1','2','3','4','5','6','7','8','9']:
                    digits.append(char)
                else:
                    sqrba+=str(char)
            ans=''.join(map(str, digits))
            if len(ans)>0 and ans!=0:
                ans_sqrba=ans_sqrba*int(ans)
            digits=[]
            sqrba=str(ans_sqrba)+sqrba

            ansbx4.delete(0,END)
            ansbx4.insert(0,str(str(cbua)+" - "+str(sqrab)+" + "+str(sqrba)+" - "+str(cbub)))
    
        topic1=ttk.Label(window1,text="1) Expansion of (x+a) (x+b)",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window1,text="Enter value of a : ",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window1,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        name_label3=ttk.Label(window1,text="Enter value of b : ",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=75)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window1,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=75)
        btn1=ttk.Button(window1,text="Calculate")
        btn1.place(x=25,y=96)
        btn1.bind("<Button>",expansionOne)
        ansbx1=ttk.Entry(window1,width=16)
        ansbx1.place(x=130,y=100)
        name_label11=ttk.Label(window1,text="Expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=125)
        c21 = PhotoImage(file = r"chapter\expansion1.png")
        c21image = c21.subsample(2,2)
        w21 = Label(window1, image=c21image)
        w21.place(x=15,y=145)

        topic2=ttk.Label(window1,text="2) Expansion of (a+b+c)² ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=330,y=35)
        name_label4=ttk.Label(window1,text="Enter value of a : ",foreground="#FF8A00",background="black")
        name_label4.place(x=350,y=55)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window1,width=16,textvariable=name_var3)
        etrybx3.place(x=455,y=55)
        name_label5=ttk.Label(window1,text="Enter value of b : ",foreground="#FF8A00",background="black")
        name_label5.place(x=350,y=75)
        name_var4=StringVar()
        etrybx4=ttk.Entry(window1,width=16,textvariable=name_var4)
        etrybx4.place(x=455,y=75)
        name_label6=ttk.Label(window1,text="Enter value of c : ",foreground="#FF8A00",background="black")
        name_label6.place(x=350,y=95)
        name_var5=StringVar()
        etrybx5=ttk.Entry(window1,width=16,textvariable=name_var5)
        etrybx5.place(x=455,y=95)
        btn2=ttk.Button(window1,text="Calculate")
        btn2.place(x=350,y=116)
        btn2.bind("<Button>",expansionTwo)
        ansbx2=ttk.Entry(window1,width=16)
        ansbx2.place(x=455,y=120)
        name_label12=ttk.Label(window1,text="Expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=335,y=145)
        c22 = PhotoImage(file = r"chapter\expansion2.png")
        c22image = c22.subsample(2,2)
        w22 = Label(window1, image=c22image)
        w22.place(x=335,y=165)

        topic3=ttk.Label(window1,text="3) Expansion of (a+b)³ ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic3.place(x=10,y=275)
        name_label7=ttk.Label(window1,text="Enter value of a : ",foreground="#FF8A00",background="black")
        name_label7.place(x=25,y=295)
        name_var6=StringVar()
        etrybx6=ttk.Entry(window1,width=16,textvariable=name_var6)
        etrybx6.place(x=130,y=295)
        name_label8=ttk.Label(window1,text="Enter value of b : ",foreground="#FF8A00",background="black")
        name_label8.place(x=25,y=315)
        name_var7=StringVar()
        etrybx7=ttk.Entry(window1,width=16,textvariable=name_var7)
        etrybx7.place(x=130,y=315)
        btn3=ttk.Button(window1,text="Calculate")
        btn3.place(x=25,y=336)
        btn3.bind("<Button>",expansionThree)
        ansbx3=ttk.Entry(window1,width=16)
        ansbx3.place(x=130,y=340)
        name_label13=ttk.Label(window1,text="Expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label13.place(x=20,y=365)
        c23 = PhotoImage(file = r"chapter\expansion3.png")
        c23image = c23.subsample(2,2)
        w23 = Label(window1, image=c23image)
        w23.place(x=15,y=385)

        topic4=ttk.Label(window1,text="4) Expansion of (a-b)³ ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic4.place(x=330,y=275)
        name_label9=ttk.Label(window1,text="Enter value of a : ",foreground="#FF8A00",background="black")
        name_label9.place(x=350,y=295)
        name_var8=StringVar()
        etrybx8=ttk.Entry(window1,width=16,textvariable=name_var8)
        etrybx8.place(x=455,y=295)
        name_label10=ttk.Label(window1,text="Enter value of b : ",foreground="#FF8A00",background="black")
        name_label10.place(x=350,y=315)
        name_var9=StringVar()
        etrybx9=ttk.Entry(window1,width=16,textvariable=name_var9)
        etrybx9.place(x=455,y=315)
        btn4=ttk.Button(window1,text="Calculate")
        btn4.place(x=350,y=336)
        btn4.bind("<Button>",expansionFour)
        ansbx4=ttk.Entry(window1,width=16)
        ansbx4.place(x=455,y=340)
        name_label14=ttk.Label(window1,text="Expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label14.place(x=335,y=365)
        c24 = PhotoImage(file = r"chapter\expansion4.png")
        c24image = c24.subsample(2,2)
        w24 = Label(window1, image=c24image)
        w24.place(x=335,y=385)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window1,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/g_7WVf6OhKU"))

        topic5=ttk.Label(window1,text="Note:- For 3 & 4 type the values of a and b only not the sign.  ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic5.place(x=190,y=600)
        c25 = PhotoImage(file = r"chapter\expansion5.png")
        c25image = c25.subsample(2,2)
        w25 = Label(window1, image=c25image)
        w25.place(x=190,y=400)
    
    from math import sqrt
    def factorisation(event=None):
        window2 = Toplevel()
        window2.title("Caltific")
        window2.resizable(width=False, height=False)
        window2.geometry("580x675+340+11")
        window2.configure(bg= 'black')
        window2.tk.call('wm', 'iconphoto', window2._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window2,text="Chapter : Factorisation",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=180,y=6)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def simplify_fraction(numer, denom):
            if denom == 0:
                return "Division by 0 - result undefined"

            common_divisor = gcd(numer, denom)
            (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)

            if common_divisor == 1:
                return (numer, denom)
            else:
                if (reduced_den > denom):
                    if (reduced_den * reduced_num < 0):
                        return(-reduced_num, -reduced_den)
                    else:
                        return (reduced_num, reduced_den)
                else:
                    return (reduced_num, reduced_den)

        def quadratic_function(event):
            a=int(name_var1.get())
            b=int(name_var2.get())
            c=int(name_var3.get())
            if (b**2-4*a*c >= 0):
                x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
                x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
                mult1 = -x1 * a
                mult2 = -x2 * a
                (num1,den1) = simplify_fraction(a,mult1)
                (num2,den2) = simplify_fraction(a,mult2)
                if ((num1 > a) or (num2 > a)):
                    ansbx1.delete(0,END)
                    ansbx1.insert(0,"No factorization")
                else:
                    if (den1 > 0):
                        sign1 = "+"
                    else:
                        sign1 = ""
                    if (den2 > 0):
                        sign2 = "+"
                    else:
                        sign2 = ""
                    ansbx1.delete(0,END)
                ansbx1.insert(0,"({}x{}{})({}x{}{})".format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
            else:
                ansbx1.delete(0,END)
                ansbx1.insert(0,"Solutions are imaginary")


        topic1=ttk.Label(window2,text="1) Factors of ax²+bx+c",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=30)
        name_label2=ttk.Label(window2,text="Enter value of a : ",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=48)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window2,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=48)
        name_label3=ttk.Label(window2,text="Enter value of b : ",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=68)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window2,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=68)
        name_label4=ttk.Label(window2,text="Enter value of c : ",foreground="#FF8A00",background="black")
        name_label4.place(x=25,y=88)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window2,width=16,textvariable=name_var3)
        etrybx3.place(x=130,y=88)
        btn1=ttk.Button(window2,text="Calculate")
        btn1.place(x=25,y=108)
        btn1.bind("<Button>",quadratic_function)
        ansbx1=ttk.Entry(window2,width=16)
        ansbx1.place(x=130,y=112)
        name_label11=ttk.Label(window2,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=135)
        c21 = PhotoImage(file = r"chapter\factorization1.png")
        c21image = c21.subsample(1,1)
        w21 = Label(window2, image=c21image)
        w21.place(x=15,y=160)

        c22 = PhotoImage(file = r"chapter\factorization2.png")
        c22image = c22.subsample(1,1)
        w22 = Label(window2, image=c22image)
        w22.place(x=15,y=400)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window2,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/2YthCDIeuig"))

        c23 = PhotoImage(file = r"chapter\factorization3.png")
        c23image = c23.subsample(1,1)
        w23 = Label(window2, image=c23image)
        w23.place(x=15,y=400)

    from math import sqrt
    
    def discount_commission(event=None):
        window3 = Toplevel()
        window3.title("Caltific")
        window3.resizable(width=False, height=False)
        window3.geometry("580x675+340+11")
        window3.configure(bg= 'black')
        window3.tk.call('wm', 'iconphoto', window3._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window3,text="Chapter : Discount and commission",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=120,y=6)

        def discount_percent(event=None):
            mp=int(name_var1.get())
            sp=int(name_var2.get())
            dp=((mp-sp)*100)/mp
            ansbx1.delete(0,END)
            ansbx1.insert(0,str(dp)+"%")

        def discount_value(event=None):
            mp=int(name_var3.get())
            d=int(name_var4.get())
            dv=mp-(mp*(d/100))
            ansbx2.delete(0,END)
            ansbx2.insert(0,str(dv))

        def commission(event=None):
            sp=int(name_var5.get())
            c=int(name_var6.get())
            cv=sp*(c/100)
            ansbx3.delete(0,END)
            ansbx3.insert(0,str(cv))

        def profit(event=None):
            sp=int(name_var7.get())
            c=int(name_var8.get())
            cv=sp-(sp*(c/100))
            ansbx4.delete(0,END)
            ansbx4.insert(0,str(cv))

        topic1=ttk.Label(window3,text="1) Discount percentange",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window3,text="Enter marked price:  ",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window3,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        name_label3=ttk.Label(window3,text="Enter selling price:  ",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=75)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window3,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=75)
        btn1=ttk.Button(window3,text="Calculate")
        btn1.place(x=25,y=96)
        btn1.bind("<Button>",discount_percent)
        ansbx1=ttk.Entry(window3,width=16)
        ansbx1.place(x=130,y=100)
        name_label11=ttk.Label(window3,text="Formula",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=125)
        c21 = PhotoImage(file = r"chapter\DC1.png")
        c21image = c21.subsample(2,2)
        w21 = Label(window3, image=c21image)
        w21.place(x=15,y=145)

        topic2=ttk.Label(window3,text="2) Discount value",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=330,y=35)
        name_label4=ttk.Label(window3,text="Enter marked price:  ",foreground="#FF8A00",background="black")
        name_label4.place(x=350,y=55)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window3,width=16,textvariable=name_var3)
        etrybx3.place(x=455,y=55)
        name_label5=ttk.Label(window3,text="Enter discount (%):  ",foreground="#FF8A00",background="black")
        name_label5.place(x=350,y=75)
        name_var4=StringVar()
        etrybx4=ttk.Entry(window3,width=16,textvariable=name_var4)
        etrybx4.place(x=455,y=75)
        btn2=ttk.Button(window3,text="Calculate")
        btn2.place(x=350,y=95)
        btn2.bind("<Button>",discount_value)
        ansbx2=ttk.Entry(window3,width=16)
        ansbx2.place(x=455,y=99)
        name_label12=ttk.Label(window3,text="Formula",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=335,y=124)
        c22 = PhotoImage(file = r"chapter\DC2.png")
        c22image = c22.subsample(3,3)
        w22 = Label(window3, image=c22image)
        w22.place(x=335,y=144)

        topic3=ttk.Label(window3,text="3) Commision value ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic3.place(x=10,y=275)
        name_label6=ttk.Label(window3,text="Enter selling price : ",foreground="#FF8A00",background="black")
        name_label6.place(x=25,y=295)
        name_var5=StringVar()
        etrybx5=ttk.Entry(window3,width=16,textvariable=name_var5)
        etrybx5.place(x=130,y=295)
        name_label7=ttk.Label(window3,text="Enter commission: ",foreground="#FF8A00",background="black")
        name_label7.place(x=25,y=315)
        name_var6=StringVar()
        etrybx6=ttk.Entry(window3,width=16,textvariable=name_var6)
        etrybx6.place(x=130,y=315)
        btn3=ttk.Button(window3,text="Calculate")
        btn3.place(x=25,y=336)
        btn3.bind("<Button>",commission)
        ansbx3=ttk.Entry(window3,width=16)
        ansbx3.place(x=130,y=340)
        name_label13=ttk.Label(window3,text="Formula",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label13.place(x=20,y=365)
        c23 = PhotoImage(file = r"chapter\DC3.png")
        c23image = c23.subsample(1,2)
        w23 = Label(window3, image=c23image)
        w23.place(x=50,y=385)


        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window3,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/htP9g_R0XuM"))

        topic4=ttk.Label(window3,text="4) Profit earned after commisiion ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic4.place(x=330,y=275)
        name_label8=ttk.Label(window3,text="Enter selling price: ",foreground="#FF8A00",background="black")
        name_label8.place(x=350,y=295)
        name_var7=StringVar()
        etrybx7=ttk.Entry(window3,width=16,textvariable=name_var7)
        etrybx7.place(x=455,y=295)
        name_label9=ttk.Label(window3,text="Enter commission: ",foreground="#FF8A00",background="black")
        name_label9.place(x=350,y=315)
        name_var8=StringVar()
        etrybx8=ttk.Entry(window3,width=16,textvariable=name_var8)
        etrybx8.place(x=455,y=315)
        btn4=ttk.Button(window3,text="Calculate")
        btn4.place(x=350,y=336)
        btn4.bind("<Button>",profit)
        ansbx4=ttk.Entry(window3,width=16)
        ansbx4.place(x=455,y=340)
        name_label14=ttk.Label(window3,text="Formula",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label14.place(x=335,y=365)
        c24 = PhotoImage(file = r"chapter\DC4.png")
        c24image = c24.subsample(2,2)
        w24 = Label(window3, image=c24image)
        w24.place(x=335,y=385)

        

    import math
    from math import sqrt
    
    def area(event=None):
        window4 = Toplevel()
        window4.title("Caltific")
        window4.resizable(width=False, height=False)
        window4.geometry("580x675+340+11")
        window4.configure(bg= 'black')
        window4.tk.call('wm', 'iconphoto', window4._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window4,text="Chapter : Area ",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=210,y=6)

        def parallelogram(event=None):
            b=int(name_var1.get())
            h=int(name_var2.get())
            ans=b*h
            ansbx1.delete(0,END)
            ansbx1.insert(0,str(ans))

        def rhombus(event=None):
            d1=int(name_var3.get())
            d2=int(name_var4.get())
            ans=0.5*(d1*d2)
            ansbx2.delete(0,END)
            ansbx2.insert(0,str(ans))
        
        def traingle(event=None):
            a=int(name_var5.get())
            b=int(name_var6.get())
            c=int(name_var7.get())
            s=(a+b+c)/2
            ans=sqrt((s)(s-a)(s-b)*(s-c))
            ansbx3.delete(0,END)
            ansbx3.insert(0,str(ans))

        def circle(event=None):
            r=int(name_var8.get())
            ans=math.pi*(r**2)
            ansbx4.delete(0,END)
            ansbx4.insert(0,str(ans))
        
        topic1=ttk.Label(window4,text="1) Area of Parallelogram",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window4,text="Enter the base:  ",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window4,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        name_label3=ttk.Label(window4,text="Enter the height:  ",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=75)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window4,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=75)
        btn1=ttk.Button(window4,text="Calculate")
        btn1.place(x=25,y=96)
        btn1.bind("<Button>",parallelogram)
        ansbx1=ttk.Entry(window4,width=16)
        ansbx1.place(x=130,y=100)
        name_label11=ttk.Label(window4,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=125)
        c21 = PhotoImage(file = r"chapter\area1.png")
        c21image = c21.subsample(2,2)
        w21 = Label(window4, image=c21image)
        w21.place(x=15,y=145)

        topic2=ttk.Label(window4,text="2) Area of Rhombus",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=330,y=35)
        name_label4=ttk.Label(window4,text="Size of diagonal 1:  ",foreground="#FF8A00",background="black")
        name_label4.place(x=350,y=55)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window4,width=16,textvariable=name_var3)
        etrybx3.place(x=455,y=55)
        name_label5=ttk.Label(window4,text="Size of diagonal 2:  ",foreground="#FF8A00",background="black")
        name_label5.place(x=350,y=75)
        name_var4=StringVar()
        etrybx4=ttk.Entry(window4,width=16,textvariable=name_var4)
        etrybx4.place(x=455,y=75)
        btn2=ttk.Button(window4,text="Calculate")
        btn2.place(x=350,y=95)
        btn2.bind("<Button>",rhombus)
        ansbx2=ttk.Entry(window4,width=16)
        ansbx2.place(x=455,y=99)
        name_label12=ttk.Label(window4,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=335,y=124)
        c22 = PhotoImage(file = r"chapter\area2.png")
        c22image = c22.subsample(3,3)
        w22 = Label(window4, image=c22image)
        w22.place(x=300,y=144)

        topic3=ttk.Label(window4,text="3) Area of traingle ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic3.place(x=10,y=275)
        name_label6=ttk.Label(window4,text="Size of side 1: ",foreground="#FF8A00",background="black")
        name_label6.place(x=25,y=295)
        name_var5=StringVar()
        etrybx5=ttk.Entry(window4,width=16,textvariable=name_var5)
        etrybx5.place(x=130,y=295)
        name_label7=ttk.Label(window4,text="Size of side 2: ",foreground="#FF8A00",background="black")
        name_label7.place(x=25,y=315)
        name_var6=StringVar()
        etrybx6=ttk.Entry(window4,width=16,textvariable=name_var6)
        etrybx6.place(x=130,y=315)
        name_label8=ttk.Label(window4,text="Size of side 3: ",foreground="#FF8A00",background="black")
        name_label8.place(x=25,y=335)
        name_var7=StringVar()
        etrybx7=ttk.Entry(window4,width=16,textvariable=name_var7)
        etrybx7.place(x=130,y=335)
        btn3=ttk.Button(window4,text="Calculate")
        btn3.place(x=25,y=356)
        btn3.bind("<Button>",traingle)
        ansbx3=ttk.Entry(window4,width=16)
        ansbx3.place(x=130,y=360)
        name_label13=ttk.Label(window4,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label13.place(x=20,y=385)
        c23 = PhotoImage(file = r"chapter\area3.png")
        c23image = c23.subsample(2,2)
        w23 = Label(window4, image=c23image)
        w23.place(x=50,y=405)

        topic4=ttk.Label(window4,text="4) Area of Circle ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic4.place(x=330,y=275)
        name_label9=ttk.Label(window4,text="Enter the radius: ",foreground="#FF8A00",background="black")
        name_label9.place(x=350,y=295)
        name_var8=StringVar()
        etrybx8=ttk.Entry(window4,width=16,textvariable=name_var8)
        etrybx8.place(x=455,y=295)
        btn4=ttk.Button(window4,text="Calculate")
        btn4.place(x=350,y=316)
        btn4.bind("<Button>",circle)
        ansbx4=ttk.Entry(window4,width=16)
        ansbx4.place(x=455,y=320)
        name_label14=ttk.Label(window4,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label14.place(x=335,y=345)
        c24 = PhotoImage(file = r"chapter\area4.png")
        c24image = c24.subsample(2,2)
        w24 = Label(window4, image=c24image)
        w24.place(x=300,y=365)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window4,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/YUT2yqNxGFY"))


        c25 = PhotoImage(file = r"chapter\area5.png")
        c25image = c25.subsample(2,2)
        w25 = Label(window4, image=c25image)
        w25.place(x=335,y=385)



    import math
    from math import sqrt
    
    def vol(event=None):
        window5 = Toplevel()
        window5.title("Caltific")
        window5.resizable(width=False, height=False)
        window5.geometry("580x675+340+11")
        window5.configure(bg= 'black')
        window5.tk.call('wm', 'iconphoto', window5._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window5,text="Chapter : Volume",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=210,y=6)

        def box(event=None):
            l=int(name_var9.get())
            b=int(name_var10.get())
            h=int(name_var11.get())
            ans=l*b*h
            ansbx5.delete(0,END)
            ansbx5.insert(0,str(ans))

        def cylinder(event=None):
            r=int(name_var12.get())
            h=int(name_var13.get())
            ans=math.pi*(r**2)*h
            ansbx6.delete(0,END)
            ansbx6.insert(0,str(ans))

        topic5=ttk.Label(window5,text="1) Volume of a rectangular box ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic5.place(x=10,y=35)
        name_label10=ttk.Label(window5,text="Enter the lenght: ",foreground="#FF8A00",background="black")
        name_label10.place(x=25,y=55)
        name_var9=StringVar()
        etrybx9=ttk.Entry(window5,width=16,textvariable=name_var9)
        etrybx9.place(x=130,y=55)
        name_label11=ttk.Label(window5,text="Enter the breadth: ",foreground="#FF8A00",background="black")
        name_label11.place(x=25,y=75)
        name_var10=StringVar()
        etrybx10=ttk.Entry(window5,width=16,textvariable=name_var10)
        etrybx10.place(x=130,y=75)
        name_label12=ttk.Label(window5,text="Enter the height: ",foreground="#FF8A00",background="black")
        name_label12.place(x=25,y=95)
        name_var11=StringVar()
        etrybx11=ttk.Entry(window5,width=16,textvariable=name_var11)
        etrybx11.place(x=130,y=95)
        btn5=ttk.Button(window5,text="Calculate")
        btn5.place(x=25,y=116)
        btn5.bind("<Button>",box)
        ansbx5=ttk.Entry(window5,width=16)
        ansbx5.place(x=130,y=120)
        name_label11=ttk.Label(window5,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=145)
        c21 = PhotoImage(file = r"chapter\volume1.png")
        c21image = c21.subsample(2,2)
        w21 = Label(window5, image=c21image)
        w21.place(x=15,y=165)

        topic6=ttk.Label(window5,text="2) Volume of clinder",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic6.place(x=330,y=35)
        name_label13=ttk.Label(window5,text="Enter the radius: ",foreground="#FF8A00",background="black")
        name_label13.place(x=350,y=55)
        name_var12=StringVar()
        etrybx12=ttk.Entry(window5,width=16,textvariable=name_var12)
        etrybx12.place(x=455,y=55)
        name_label14=ttk.Label(window5,text="Enter the height: ",foreground="#FF8A00",background="black")
        name_label14.place(x=350,y=75)
        name_var13=StringVar()
        etrybx13=ttk.Entry(window5,width=16,textvariable=name_var13)
        etrybx13.place(x=455,y=75)
        btn6=ttk.Button(window5,text="Calculate")
        btn6.place(x=350,y=96)
        btn6.bind("<Button>",cylinder)
        ansbx6=ttk.Entry(window5,width=16)
        ansbx6.place(x=455,y=100)
        name_label12=ttk.Label(window5,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=335,y=124)
        c22 = PhotoImage(file = r"chapter\volume2.png")
        c22image = c22.subsample(3,3)
        w22 = Label(window5, image=c22image)
        w22.place(x=335,y=144)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window5,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/YUT2yqNxGFY"))


        c23 = PhotoImage(file = r"chapter\volume3.png")
        c23image = c23.subsample(3,3)
        w23 = Label(window5, image=c23image)
        w23.place(x=335,y=144)

        
    cm1 = PhotoImage(file = r"chapter\1m.png")
    cm1img = cm1.subsample(1,1)
    cm1 = Button(mat_sum, text="", fg="black",image=cm1img, bd=0, bg="black", cursor="hand2",
                 )
    cm1.bind('<Button>', indices)
    cm1.place(x=3,y=5)

    cm2 = PhotoImage(file = r"chapter\2m.png")
    cm2img = cm2.subsample(1,1)
    cm2 = Button(mat_sum, text="", fg="black",image=cm2img, bd=0, bg="black", cursor="hand2",
                 )
    cm2.bind('<Button>', expansion)
    cm2.place(x=3,y=60)

    cm3 = PhotoImage(file = r"chapter\3m.png")
    cm3img = cm3.subsample(1,1)
    cm3 = Button(mat_sum, text="", fg="black",image=cm3img, bd=0, bg="black", cursor="hand2",
                 )
    cm3.bind('<Button>', factorisation)
    cm3.place(x=3,y=115)

    cm4 = PhotoImage(file = r"chapter\4m.png")
    cm4img = cm4.subsample(1,1)
    cm4 = Button(mat_sum, text="", fg="black",image=cm4img, bd=0, bg="black", cursor="hand2",
                 )
    cm4.bind('<Button>', discount_commission)
    cm4.place(x=3,y=170)

    cm5 = PhotoImage(file = r"chapter\5m.png")
    cm5img = cm5.subsample(1,1)
    cm5 = Button(mat_sum, text="", fg="black",image=cm5img, bd=0, bg="black", cursor="hand2",
                 )
    cm5.bind('<Button>', area)
    cm5.place(x=3,y=225)

    cm6 = PhotoImage(file = r"chapter\6m.png")
    cm6img = cm6.subsample(1,1)
    cm6 = Button(mat_sum, text="", fg="black",image=cm6img, bd=0, bg="black", cursor="hand2",
                 )
    cm6.bind('<Button>', vol)
    cm6.place(x=3,y=280)

   
    def force_and_pressure(event=None):
        window6 = Toplevel()
        window6.title("Caltific")
        window6.resizable(width=False, height=False)
        window6.geometry("580x675+340+11")
        window6.configure(bg= 'black')
        window6.tk.call('wm', 'iconphoto', window6._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window6,text="Chapter : Force and Pressure",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=170,y=6)

        def force(event=None):
            m=int(name_var1.get())
            a=int(name_var2.get())
            ans=m*a
            ansbx1.delete(0,END)
            ansbx1.insert(0,str(ans))

        def pressure(event=None):
            f=int(name_var3.get())
            a=int(name_var4.get())
            ans=f/a
            ansbx2.delete(0,END)
            ansbx2.insert(0,str(ans))
        
        def density(event=None):
            m=int(name_var5.get())
            v=int(name_var6.get())
            ans=m/v
            ansbx3.delete(0,END)
            ansbx3.insert(0,str(ans))

        def rdensity(event=None):
            e=int(name_var7.get())
            w=int(name_var8.get())
            ans=e/w
            ansbx4.delete(0,END)
            ansbx4.insert(0,str(ans))

        topic1=ttk.Label(window6,text="1) Force: ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window6,text="Mass(SI):  ",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window6,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        name_label3=ttk.Label(window6,text="Acceleration(SI):  ",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=75)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window6,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=75)
        btn1=ttk.Button(window6,text="Calculate")
        btn1.place(x=25,y=96)
        btn1.bind("<Button>",force)
        ansbx1=ttk.Entry(window6,width=16)
        ansbx1.place(x=130,y=100)
        name_label11=ttk.Label(window6,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=125)
        c21 = PhotoImage(file = r"chapter\fp1.png")
        c21image = c21.subsample(2,2)
        w21 = Label(window6, image=c21image)
        w21.place(x=20,y=145)

        topic2=ttk.Label(window6,text="2) Pressure",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=330,y=35)
        name_label4=ttk.Label(window6,text="Force(SI):  ",foreground="#FF8A00",background="black")
        name_label4.place(x=350,y=55)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window6,width=16,textvariable=name_var3)
        etrybx3.place(x=455,y=55)
        name_label5=ttk.Label(window6,text="Area(SI):  ",foreground="#FF8A00",background="black")
        name_label5.place(x=350,y=75)
        name_var4=StringVar()
        etrybx4=ttk.Entry(window6,width=16,textvariable=name_var4)
        etrybx4.place(x=455,y=75)
        btn2=ttk.Button(window6,text="Calculate")
        btn2.place(x=350,y=95)
        btn2.bind("<Button>",pressure)
        ansbx2=ttk.Entry(window6,width=16)
        ansbx2.place(x=455,y=100)
        name_label12=ttk.Label(window6,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=335,y=124)
        c22 = PhotoImage(file = r"chapter\fp2.png")
        c22image = c22.subsample(2,2)
        w22 = Label(window6, image=c22image)
        w22.place(x=335,y=144)

        topic3=ttk.Label(window6,text="3) Density ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic3.place(x=10,y=275)
        name_label6=ttk.Label(window6,text="Mass(SI): ",foreground="#FF8A00",background="black")
        name_label6.place(x=25,y=295)
        name_var5=StringVar()
        etrybx5=ttk.Entry(window6,width=16,textvariable=name_var5)
        etrybx5.place(x=130,y=295)
        name_label7=ttk.Label(window6,text="Volume(SI): ",foreground="#FF8A00",background="black")
        name_label7.place(x=25,y=315)
        name_var6=StringVar()
        etrybx6=ttk.Entry(window6,width=16,textvariable=name_var6)
        etrybx6.place(x=130,y=315)
        btn3=ttk.Button(window6,text="Calculate")
        btn3.place(x=25,y=336)
        btn3.bind("<Button>",density)
        ansbx3=ttk.Entry(window6,width=16)
        ansbx3.place(x=130,y=340)
        name_label13=ttk.Label(window6,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label13.place(x=20,y=365)
        c23 = PhotoImage(file = r"chapter\fp3.png")
        c23image = c23.subsample(7,7)
        w23 = Label(window6, image=c23image)
        w23.place(x=20,y=385)

        topic4=ttk.Label(window6,text="4) Relative Density ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic4.place(x=330,y=275)
        name_label8=ttk.Label(window6,text="Density of Element:",foreground="#FF8A00",background="black")
        name_label8.place(x=350,y=295)
        name_var7=StringVar()
        etrybx7=ttk.Entry(window6,width=16,textvariable=name_var7)
        etrybx7.place(x=455,y=295)
        name_label9=ttk.Label(window6,text="Density of Water: ",foreground="#FF8A00",background="black")
        name_label9.place(x=350,y=315)
        name_var8=StringVar()
        etrybx8=ttk.Entry(window6,width=16,textvariable=name_var8)
        etrybx8.place(x=455,y=315)
        btn4=ttk.Button(window6,text="Calculate")
        btn4.place(x=350,y=336)
        btn4.bind("<Button>",rdensity)
        ansbx4=ttk.Entry(window6,width=16)
        ansbx4.place(x=455,y=340)
        name_label14=ttk.Label(window6,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label14.place(x=335,y=365)
        c24 = PhotoImage(file = r"chapter\fp4.png")
        c24image = c24.subsample(2,2)
        w24 = Label(window6, image=c24image)
        w24.place(x=335,y=385)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window6,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/g1kMb7DTIuM"))

        c25 = PhotoImage(file = r"chapter\fp5.png")
        c25image = c25.subsample(2,2)
        w25 = Label(window6, image=c25image)
        w25.place(x=335,y=385)


    def atoms(event=None):
        window7 = Toplevel()
        window7.title("Caltific")
        window7.resizable(width=False, height=False)
        window7.geometry("580x675+340+11")
        window7.configure(bg= 'black')
        window7.tk.call('wm', 'iconphoto', window7._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window7,text="Chapter : Atoms",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=120,y=6)

        def atomic(event=None):
            m=name_var1.get()
            array=[
                'H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V',
                'Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh',
                'Pd','Ag','Cd','In','Sn','Sb','Te','L','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg',
                'Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu''Am','Cm','Bk','Cf','Es','Fm','Md','No',
                'Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Uub','Uuq'
            ]
            if m in array:
                ans=(array.index(m))+1
            else:
                ans="Element Not Found"
            ansbx1.delete(0,END)
            ansbx1.insert(0,str(ans))

        def conf(event=None):
            e=name_var3.get()
            array=[
                'H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V',
                'Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh',
                'Pd','Ag','Cd','In','Sn','Sb','Te','L','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg',
                'Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu''Am','Cm','Bk','Cf','Es','Fm','Md','No',
                'Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Uub','Uuq'
            ]
            if e in array:
                atomic=(array.index(e))+1
                ans=''
                k,l,m,n,o=2,8,18,32,50
                if atomic>0:
                    if atomic>=k:
                        k=2
                    else:
                        k=atomic
                    ans+=str(k)+" "
                    atomic-=k
                if atomic>0:
                    if atomic>=l:
                        l=8
                    else:
                        l=atomic
                    ans+=str(l)+" "
                    atomic-=l
                if atomic>0:
                    if atomic>=m:
                        m=18
                    else:
                        m=atomic
                    ans+=str(m)+" "
                    atomic-=m
                if atomic>0:
                    if atomic>=n:
                        n=32
                    else:
                        n=atomic
                    ans+=str(n)+" "
                    atomic-=n
                if atomic>0:
                    if atomic>=o:
                        o=50
                    else:
                        o=atomic
                    ans+=str(o)+" "
                    atomic-=o
            else:
                ans="Element Not Found"
            ansbx2.delete(0,END)
            ansbx2.insert(0,str(ans))
        

        topic1=ttk.Label(window7,text="1) Atomic Number: ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window7,text="Enter the element:",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window7,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        btn1=ttk.Button(window7,text="Calculate")
        btn1.place(x=25,y=76)
        btn1.bind("<Button>",atomic)
        ansbx1=ttk.Entry(window7,width=16)
        ansbx1.place(x=130,y=80)
        name_label11=ttk.Label(window7,text="Expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=105)
        c21 = PhotoImage(file = r"chapter\at1.png")
        c21image = c21.subsample(2,2)
        w21 = Label(window7, image=c21image)
        w21.place(x=15,y=125)
        

        topic2=ttk.Label(window7,text="2) No. of e- in Each shell",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=10,y=380)
        name_label4=ttk.Label(window7,text="Enter the element:",foreground="#FF8A00",background="black")
        name_label4.place(x=25,y=400)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window7,width=16,textvariable=name_var3)
        etrybx3.place(x=130,y=400)
        btn2=ttk.Button(window7,text="Calculate")
        btn2.place(x=25,y=421)
        btn2.bind("<Button>",conf)
        ansbx2=ttk.Entry(window7,width=16)
        ansbx2.place(x=130,y=425)
        name_label12=ttk.Label(window7,text="Expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=20,y=450)
        c22 = PhotoImage(file = r"chapter\at2.png")
        c22image = c22.subsample(1,1)
        w22 = Label(window7, image=c22image)
        w22.place(x=15,y=470)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window7,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.place(x=470,y=650)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/jED-hPZhfqM"))

        c23 = PhotoImage(file = r"chapter\at3.png")
        c23image = c23.subsample(2,2)
        w23 = Label(window7, image=c23image)
        w23.place(x=15,y=385)



    def effect_of_heat(event=None):
        window8 = Toplevel()
        window8.title("Caltific")
        window8.resizable(width=False, height=False)
        window8.geometry("580x400+340+11")
        window8.configure(bg= 'black')
        window8.tk.call('wm', 'iconphoto', window8._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window8,text="Chapter : Effect of heat",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=180,y=6)

        def spcheat(event=None):
            m=name_var1.get()
            array={
                'Aluminium': 0.21,
                'Alcohol': 0.58,
                'Gold': 0.03,
                'Hydrogen': 3.42,
                'Iron': 0.11,
                'Copper': 0.09,
                'Mercury':0.03,
                'Water':1,
            }
            if m in array:
                ans=array[m]
            else:
                ans="Element Not Found"
            ansbx1.delete(0,END)
            ansbx1.insert(0,str(ans))

        def conf(event=None):
            m=name_var2.get()
            array={
                'Copper':17,
                'Aluminium':23.1,
                'Iron':11.5,
                'Silver':18,
                'Alcohol': 1,
                'Water':0.2,
                'Mercury':0.2,
                'Chloroform': 1.3
            }
            if m in array:
                ans=array[m]
            else:
                ans="Element Not Found"
            ansbx2.delete(0,END)
            ansbx2.insert(0,str(ans))
        

        topic1=ttk.Label(window8,text="1) Specific Heat ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window8,text="Enter the element:",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window8,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        btn1=ttk.Button(window8,text="Calculate")
        btn1.place(x=25,y=76)
        btn1.bind("<Button>",spcheat)
        ansbx1=ttk.Entry(window8,width=16)
        ansbx1.place(x=130,y=80)
        name_label11=ttk.Label(window8,text="Expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=105)
        c21 = PhotoImage(file = r"chapter\sh1.png")
        c21image = c21.subsample(2,2)
        w21 = Label(window8, image=c21image)
        w21.place(x=15,y=125)

        topic2=ttk.Label(window8,text="2) Coefficient of linear expansion",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=330,y=35)
        name_label3=ttk.Label(window8,text="Enter the element:",foreground="#FF8A00",background="black")
        name_label3.place(x=350,y=55)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window8,width=16,textvariable=name_var2)
        etrybx2.place(x=455,y=55)
        btn2=ttk.Button(window8,text="Calculate")
        btn2.place(x=350,y=76)
        btn2.bind("<Button>",conf)
        ansbx2=ttk.Entry(window8,width=16)
        ansbx2.place(x=455,y=80)
        name_label12=ttk.Label(window8,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=335,y=105)
        c22 = PhotoImage(file = r"chapter\sh2.png")
        c22image = c22.subsample(2,2)
        w22 = Label(window8, image=c22image)
        w22.place(x=335,y=125)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window8,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/T_hf_Fn5S_w"))

        c23 = PhotoImage(file = r"chapter\sh3.png")
        c23image = c23.subsample(2,2)
        w23 = Label(window8, image=c23image)
        w23.place(x=15,y=385)

    def DAS(event=None):
        window9 = Toplevel()
        window9.title("Caltific")
        window9.resizable(width=False, height=False)
        window9.geometry("580x400+340+11")
        window9.configure(bg= 'black')
        window9.tk.call('wm', 'iconphoto', window9._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window9,text="Chapter : Distance and Speed",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=160,y=6)

        def speed(event=None):
            d=int(name_var1.get())
            t=int(name_var2.get())
            ans=d/t
            ansbx1.delete(0,END)
            ansbx1.insert(0,str(ans))

        def avgSpeed(event=None):
            d=int(name_var3.get())
            t=int(name_var4.get())
            ans=d/t
            ansbx2.delete(0,END)
            ansbx2.insert(0,str(ans))

        def avgSpeedDSame(event=None):
            a=int(name_var5.get())
            b=int(name_var6.get())
            ans=(2*a*b)/(a+b)
            ansbx3.delete(0,END)
            ansbx3.insert(0,str(ans))

        

        topic1=ttk.Label(window9,text="1) Speed ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window9,text="Enter the Distance:",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window9,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        name_label3=ttk.Label(window9,text="Enter the time:",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=75)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window9,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=75)
        btn1=ttk.Button(window9,text="Calculate")
        btn1.place(x=25,y=96)
        btn1.bind("<Button>",speed)
        ansbx1=ttk.Entry(window9,width=16)
        ansbx1.place(x=130,y=100)
        name_label11=ttk.Label(window9,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=125)
        c21 = PhotoImage(file = r"chapter\DAS1.png")
        c21image = c21.subsample(3,2)
        w21 = Label(window9, image=c21image)
        w21.place(x=20,y=145)

        topic2=ttk.Label(window9,text="2) Average Speed",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=330,y=35)
        name_label4=ttk.Label(window9,text="Distance travelled:",foreground="#FF8A00",background="black")
        name_label4.place(x=350,y=55)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window9,width=16,textvariable=name_var3)
        etrybx3.place(x=455,y=55)
        name_label5=ttk.Label(window9,text="Time taken:",foreground="#FF8A00",background="black")
        name_label5.place(x=350,y=75)
        name_var4=StringVar()
        etrybx4=ttk.Entry(window9,width=16,textvariable=name_var4)
        etrybx4.place(x=455,y=75)
        btn2=ttk.Button(window9,text="Calculate")
        btn2.place(x=350,y=96)
        btn2.bind("<Button>",avgSpeed)
        ansbx2=ttk.Entry(window9,width=16)
        ansbx2.place(x=455,y=100)
        name_label12=ttk.Label(window9,text="Explanation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=335,y=124)
        c22 = PhotoImage(file = r"chapter\DAS2.png")
        c22image = c22.subsample(3,2)
        w22 = Label(window9, image=c22image)
        w22.place(x=335,y=144)

        topic1=ttk.Label(window9,text="1) Average Speed when Distance travelled is same ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=275)
        name_label6=ttk.Label(window9,text="First half Speed:",foreground="#FF8A00",background="black")
        name_label6.place(x=25,y=295)
        name_var5=StringVar()
        etrybx5=ttk.Entry(window9,width=16,textvariable=name_var5)
        etrybx5.place(x=130,y=295)
        name_label7=ttk.Label(window9,text="Second half Speed:",foreground="#FF8A00",background="black")
        name_label7.place(x=25,y=315)
        name_var6=StringVar()
        etrybx6=ttk.Entry(window9,width=16,textvariable=name_var6)
        etrybx6.place(x=130,y=315)
        btn3=ttk.Button(window9,text="Calculate")
        btn3.place(x=25,y=336)
        btn3.bind("<Button>", avgSpeedDSame)
        ansbx3=ttk.Entry(window9,width=16)
        ansbx3.place(x=130,y=340)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window9,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback("https://youtu.be/SUZ0PDCF890"))
    
        c23 = PhotoImage(file = r"chapter\DAS3.png")
        c23image = c23.subsample(7,7)
        w23 = Label(window9, image=c23image)
        w23.place(x=20,y=385)

    import tkinter.messagebox

    def df(event=None):
        window10 = Toplevel()
        window10.title("Caltific")
        window10.resizable(width=False, height=False)
        window10.geometry("580x690+340+11")
        window10.configure(bg= 'black')
        window10.tk.call('wm', 'iconphoto', window10._w, PhotoImage(file='images/caltific.png'))

        name_label1=ttk.Label(window10,text="Chapter : Conversion of values",foreground="#FF8A00",background="black",font= ('Helvetica bold',15,BOLD,UNDERLINE))
        name_label1.place(x=160,y=6)

        def distance(event=None):
            mili=name_var1.get()
            centi=name_var2.get()
            metr=name_var3.get()
            kilo=name_var4.get()
            var=0
            if len(mili)!=0:
                var+=1
            if len(centi)!=0:
                var+=1
            if len(metr)!=0:
                var+=1
            if len(kilo)!=0:
                var+=1
            if var !=1:
                tkinter.messagebox.showerror("Error", "Enter only on field")
                etrybx1.delete(0,END)
                etrybx2.delete(0,END)
                etrybx3.delete(0,END)
                etrybx4.delete(0,END)
            if len(mili):
                mili=float(mili)
                centi=mili/10
                metr=mili/1000
                kilo=mili/10000
                etrybx2.delete(0,END)
                etrybx3.delete(0,END)
                etrybx4.delete(0,END)
                etrybx2.insert(0,str(centi))
                etrybx3.insert(0,str(metr))
                etrybx4.insert(0,str(kilo))
                return


            if len(centi):
                centi=float(centi)
                mili=centi*10
                metr=centi/10
                kilo=centi/1000
                etrybx1.delete(0,END)
                etrybx3.delete(0,END)
                etrybx4.delete(0,END)
                etrybx1.insert(0,str(mili))
                etrybx3.insert(0,str(metr))
                etrybx4.insert(0,str(kilo))
                return

            if len(metr):
                metr=float(metr)
                mili=metr*1000
                centi=metr*100
                kilo=metr/1000
                etrybx1.delete(0,END)
                etrybx2.delete(0,END)
                etrybx4.delete(0,END)
                etrybx1.insert(0,str(mili))
                etrybx2.insert(0,str(centi))
                etrybx4.insert(0,str(kilo))
                return
            
            if len(kilo):
                kilo=int(kilo)
                mili=kilo*10000
                centi=kilo*1000
                metr=kilo*100
                etrybx1.delete(0,END)
                etrybx2.delete(0,END)
                etrybx3.delete(0,END)
                etrybx1.insert(0,str(mili))
                etrybx2.insert(0,str(centi))
                etrybx3.insert(0,str(metr))
                return

        def temp(event=None):
            degree=name_var5.get()
            farhan=name_var6.get()
            var=0
            if len(degree)!=0:
                var+=1
            if len(farhan)!=0:
                var+=1
            if var !=1:
                tkinter.messagebox.showerror("Error", "Enter only on field")
                etrybx5.delete(0,END)
                etrybx6.delete(0,END)
            
            if len(degree):
                degree=float(degree)
                farhan=(degree*(9/5))+32
                etrybx6.delete(0,END)
                etrybx6.insert(0,str(farhan))
                return

            if len(farhan):
                farhan=float(farhan)
                degree=(farhan-32)/(9/5)
                etrybx5.delete(0,END)
                etrybx5.insert(0,str(degree))
                return


        def clear(*args,event=None):
            etrybx1.delete(0,END)
            etrybx2.delete(0,END)
            etrybx3.delete(0,END)
            etrybx4.delete(0,END)
            etrybx5.delete(0,END)
            etrybx6.delete(0,END)

        topic1=ttk.Label(window10,text="1) Distance ",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic1.place(x=10,y=35)
        name_label2=ttk.Label(window10,text="Millimeter:",foreground="#FF8A00",background="black")
        name_label2.place(x=25,y=55)
        name_var1=StringVar()
        etrybx1=ttk.Entry(window10,width=16,textvariable=name_var1)
        etrybx1.place(x=130,y=55)
        name_label3=ttk.Label(window10,text="Centimeter:",foreground="#FF8A00",background="black")
        name_label3.place(x=25,y=75)
        name_var2=StringVar()
        etrybx2=ttk.Entry(window10,width=16,textvariable=name_var2)
        etrybx2.place(x=130,y=75)
        name_label4=ttk.Label(window10,text="Meter:",foreground="#FF8A00",background="black")
        name_label4.place(x=25,y=95)
        name_var3=StringVar()
        etrybx3=ttk.Entry(window10,width=16,textvariable=name_var3)
        etrybx3.place(x=130,y=95)
        name_label5=ttk.Label(window10,text="KiloMeter:",foreground="#FF8A00",background="black")
        name_label5.place(x=25,y=115)
        name_var4=StringVar()
        etrybx4=ttk.Entry(window10,width=16,textvariable=name_var4)
        etrybx4.place(x=130,y=115)
        btn1=ttk.Button(window10,text="Calculate")
        btn1.place(x=25,y=145)
        btn1.bind("<Button>",distance)
        clr=ttk.Button(window10, text="Clear")
        clr.place(x=145, y=145)
        clr.bind("<Button>",clear)
        name_label11=ttk.Label(window10,text="Units",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label11.place(x=20,y=170)
        c21 = PhotoImage(file = r"chapter\di1.png")
        c21image = c21.subsample(1,1)
        w21 = Label(window10, image=c21image)
        w21.place(x=20,y=190)

        topic2=ttk.Label(window10,text="2) Temperature",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD))
        topic2.place(x=10,y=460)
        name_label6=ttk.Label(window10,text="Degree:",foreground="#FF8A00",background="black")
        name_label6.place(x=25,y=480)
        name_var5=StringVar()
        etrybx5=ttk.Entry(window10,width=16,textvariable=name_var5)
        etrybx5.place(x=130,y=480)
        name_label7=ttk.Label(window10,text="Fahrenheit:",foreground="#FF8A00",background="black")
        name_label7.place(x=25,y=500)
        name_var6=StringVar()
        etrybx6=ttk.Entry(window10,width=16,textvariable=name_var6)
        etrybx6.place(x=130,y=500)
        btn2=ttk.Button(window10,text="Calculate")
        btn2.place(x=25,y=530)
        btn2.bind("<Button>",temp)
        clr=ttk.Button(window10, text="Clear")
        clr.place(x=145, y=530)
        clr.bind("<Button>",clear)   
        name_label12=ttk.Label(window10,text="Relation",foreground="#FF8A00",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE))
        name_label12.place(x=20,y=570)
        c22 = PhotoImage(file = r"chapter\di2.png")
        c22image = c22.subsample(1,2)
        w22 = Label(window10, image=c22image)
        w22.place(x=20,y=590)

        def callback(url):
            webbrowser.open_new_tab(url)
        link=ttk.Label(window10,text="Refer this video",foreground="#03a5fc",background="black",font= ('Helvetica bold',10,BOLD,UNDERLINE),cursor="hand2")
        link.pack(side=BOTTOM)
        link.bind("<Button-1>", lambda e: callback(""))

        c23 = PhotoImage(file = r"chapter\di3.png")
        c23image = c23.subsample(7,7)
        w23 = Label(window10, image=c23image)
        w23.place(x=20,y=385)

    cs1 = PhotoImage(file = r"chapter\1s.png")
    cs1img = cs1.subsample(1,1)
    cs1 = Button(sci_sum, text="", fg="black",image=cs1img, bd=0, bg="black", cursor="hand2",
                 )
    cs1.bind('<Button>', force_and_pressure)
    cs1.place(x=3,y=5)

    cs2 = PhotoImage(file = r"chapter\2s.png")
    cs2img = cs2.subsample(1,1)
    cs2 = Button(sci_sum, text="", fg="black",image=cs2img, bd=0, bg="black", cursor="hand2",
                 )
    cs2.bind('<Button>', atoms)
    cs2.place(x=3,y=60)

    cs3 = PhotoImage(file = r"chapter\3s.png")
    cs3img = cs3.subsample(1,1)
    cs3 = Button(sci_sum, text="", fg="black",image=cs3img, bd=0, bg="black", cursor="hand2",
                 )
    cs3.bind('<Button>', effect_of_heat)
    cs3.place(x=3,y=115)

    cs4 = PhotoImage(file = r"chapter\4s.png")
    cs4img = cs4.subsample(1,1)
    cs4 = Button(sci_sum, text="", fg="black",image=cs4img, bd=0, bg="black", cursor="hand2",
                 )
    cs4.bind('<Button>', DAS)
    cs4.place(x=3,y=170)

    cs5 = PhotoImage(file = r"chapter\5s.png")
    cs5img = cs5.subsample(1,1)
    cs5 = Button(sci_sum, text="", fg="black",image=cs5img, bd=0, bg="black", cursor="hand2",
                 )
    cs5.bind('<Button>', df)
    cs5.place(x=3,y=225)

    window.mainloop()

root.after(3000, main_window)
          
root.mainloop() 