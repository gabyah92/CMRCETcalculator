from tkinter import *

root = Tk()
result = float()
check = 0

def button1():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'1')
    entry.config(state='readonly')

def button2():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'2')
    entry.config(state='readonly')

def button3():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'3')
    entry.config(state='readonly')

def button4():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'4')
    entry.config(state='readonly')

def button5():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'5')
    entry.config(state='readonly')

def button6():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'6')
    entry.config(state='readonly')

def button7():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'7')
    entry.config(state='readonly')

def button8():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'8')
    entry.config(state='readonly')

def button9():
    entry.config(state='normal')
    if entry.get() == '0':
        entry.delete(0,END)
    entry.insert(INSERT,'9')
    entry.config(state='readonly')

def button0():
    if entry.get()=='' or entry.get()[0] == '0' or entry.get()[-1:] in '+-/*^%':
        return
    entry.config(state='normal')
    entry.insert(INSERT,'0')
    entry.config(state='readonly')

def plus():
    if entry.get()[-1:] in '+-/*^%':
        return
    global check
    check = 0
    entry.config(state='normal')
    entry.insert(END, '+')
    entry.config(state='readonly')

def minus():
    if entry.get()[-1:] in '-':
        return
    global check
    check = 0
    entry.config(state='normal')
    entry.insert(END, '-')
    entry.config(state='readonly')

def div():
    if entry.get()[-1:] in '+-/*^%':
        return
    global check
    check = 0
    entry.config(state='normal')
    entry.insert(END, '/')
    entry.config(state='readonly')

def mul():
    if entry.get()[-1:] in '+-/*^%':
        return
    global check
    check = 0
    entry.config(state='normal')
    entry.insert(END, '*')
    entry.config(state='readonly')

def pow():
    if entry.get()[-1:] in '+-/*^%':
        return
    global check
    check = 0
    entry.config(state='normal')
    entry.insert(END, '^')
    entry.config(state='readonly')

def mod():
    if entry.get()[-1:] in '+-/*^%':
        return
    global check
    check = 0
    entry.config(state='normal')
    entry.insert(END, '%')
    entry.config(state='readonly')

def dotto():
    global check
    if check==1:
        return
    check = 1
    entry.config(state='normal')
    entry.insert(END, '.')
    entry.config(state='readonly')

def equals():
    entry.config(state='normal')
    try:
        if entry.get() == '':
            return
        if entry.get()[-1:] == '.' and entry.get()[-2] in '+-/*^%':
            k = eval(''.join((entry.get()[:-2]).replace('^', '**')))
        elif entry.get()[-1:] in '+-/*^%.':
            k = eval(''.join((entry.get()[:-1]).replace('^', '**')))
        else:
            k = eval(''.join(entry.get().replace('^', '**')))
        entry.delete(0,END)
        if len(str(k))>=15:
            entry.insert(INSERT,f'{k:.15f}')
        else:
            entry.insert(INSERT,k)
        entry.config(state='readonly')
    except ArithmeticError:
        entry.delete(0, END)
        entry.insert(INSERT, 'INF')
        entry.config(state='readonly')
    except Exception:
        entry.delete(0, END)
        entry.insert(INSERT, 'ERROR')
        entry.config(state='readonly')

def clear():
    global check
    check = 0
    entry.config(state='normal')
    entry.delete(0, END)
    entry.insert(INSERT, 0)
    entry.config(state='readonly')

root.title('Calculator')
root.config(bg='#289CA6')
root.geometry('480x520+700+200')
root.maxsize(480,520)
root.minsize(480,520)

entry = Entry(highlightthickness=5,highlightbackground='black',bg='lightyellow',font='sans 37 bold',state='readonly')
entry.place(x=10,y=10,width=460,height=70)

allclear = Button(text='C',bg='orange',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=clear)
allclear.place(x=10,y=85,width=100,height=80)

butplus = Button(text='+',bg='grey',font='sans 50 bold',borderwidth=4,activebackground='black',activeforeground='white',command=plus)
butplus.place(x=130,y=85,width=100,height=80)

butmod = Button(text='%',bg='grey',font='sans 40 bold',borderwidth=4,activebackground='black',activeforeground='white',command=mod)
butmod.place(x=250,y=85,width=100,height=80)

butpow = Button(text='^',bg='grey',font='sans 50 bold',borderwidth=4,activebackground='black',activeforeground='white',command=pow)
butpow.place(x=370,y=85,width=100,height=80)

but1 = Button(text='1',activebackground='black',activeforeground='white',bg='lightpink',font='sans 30 bold',borderwidth=4,command=button1)
but1.place(x=10,y=170,width=100,height=80)

but2 = Button(text='2',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button2)
but2.place(x=130,y=170,width=100,height=80)

but3 = Button(text='3',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button3)
but3.place(x=250,y=170,width=100,height=80)

but4 = Button(text='4',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button4)
but4.place(x=10,y=255,width=100,height=80)

but5 = Button(text='5',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button5)
but5.place(x=130,y=255,width=100,height=80)

but6 = Button(text='6',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button6)
but6.place(x=250,y=255,width=100,height=80)

but7 = Button(text='7',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button7)
but7.place(x=10,y=340,width=100,height=80)

but8 = Button(text='8',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button8)
but8.place(x=130,y=340,width=100,height=80)

but9 = Button(text='9',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button9)
but9.place(x=250,y=340,width=100,height=80)

butdot = Button(text='.',bg='grey',font='sans 50 bold',borderwidth=4,activebackground='black',activeforeground='white',command=dotto)
butdot.place(x=10,y=425,width=100,height=80)

but0 = Button(text='0',bg='lightpink',font='sans 30 bold',borderwidth=4,activebackground='black',activeforeground='white',command=button0)
but0.place(x=130,y=425,width=100,height=80)

butminus = Button(text='-',bg='grey',font='sans 70',borderwidth=4,activebackground='black',activeforeground='white',command=minus)
butminus.place(x=250,y=425,width=100,height=80)

butequals = Button(text='=',bg='darkred',fg='lightyellow',font='sans 70 bold',borderwidth=4,activebackground='red',activeforeground='white',command=equals)
butequals.place(x=370,y=340,width=100,height=165)

butmul = Button(text='*',bg='grey',font='sans 50 bold',borderwidth=4,activebackground='black',activeforeground='white',command=mul)
butmul.place(x=370,y=255,width=100,height=80)

butdiv = Button(text='/',bg='grey',font='sans 50 bold',borderwidth=4,activebackground='black',activeforeground='white',command=div)
butdiv.place(x=370,y=170,width=100,height=80)

root.mainloop()