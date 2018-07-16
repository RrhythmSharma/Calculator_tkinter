from tkinter import *

win = Tk()
win.geometry("220x285")
win.title('Calculator')
win.minsize(220, 285)
win.maxsize(220, 285)
win.config(bg='light yellow')

win.rowconfigure(0, weight=2)
win.rowconfigure(2, weight=1)
win.rowconfigure(3, weight=1)
win.rowconfigure(4, weight=1)
win.rowconfigure(5, weight=1)
win.rowconfigure(6, weight=1)
win.rowconfigure(7, weight=1)

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
win.columnconfigure(3, weight=1)
win.columnconfigure(4, weight=1)

result = Entry(win, relief=SUNKEN, font="Helvetica 15 ", fg='black', bg='light blue')
result.grid(row=0, column=0, sticky='news', rowspan=2, columnspan=5)

frame = Frame(win).grid(row=2, column=0, rowspan=1)
# create 0-9 button
button0 = Button(win, text='0', width=4, command=lambda: set_text('0'), fg='black', bg='light green')
button1 = Button(win, text='1', width=4, command=lambda: set_text('1'), fg='black', bg='light green')
button2 = Button(win, text='2', width=4, command=lambda: set_text('2'), fg='black', bg='light green')
button3 = Button(win, text='3', width=4, command=lambda: set_text('3'), fg='black', bg='light green')
button4 = Button(win, text='4', width=4, command=lambda: set_text('4'), fg='black', bg='light green')
button5 = Button(win, text='5', width=4, command=lambda: set_text('5'), fg='black', bg='light green')
button6 = Button(win, text='6', width=4, command=lambda: set_text('6'), fg='black', bg='light green')
button7 = Button(win, text='7', width=4, command=lambda: set_text('7'), fg='black', bg='light green')
button8 = Button(win, text='8', width=4, command=lambda: set_text('8'), fg='black', bg='light green')
button9 = Button(win, text='9', width=4, command=lambda: set_text('9'), fg='black', bg='light green')
# grid 0-9
button0.grid(row=4, column=0, stick='e')
button1.grid(row=4, column=1, stick='e')
button2.grid(row=4, column=2, stick='e')
button3.grid(row=5, column=0, stick='e')
button4.grid(row=5, column=1, stick='e')
button5.grid(row=5, column=2, stick='e')
button6.grid(row=6, column=0, stick='e')
button7.grid(row=6, column=1, stick='e')
button8.grid(row=6, column=2, stick='e')
button9.grid(row=7, column=0, stick='e')
# create arithmetic button
plusbutton = Button(win, text='+', width=4, command=lambda: [set_text('+')], fg='black', bg='light green')
mulbutton = Button(win, text='*', width=4, command=lambda: set_text('*'), fg='black', bg='light green')
minusbutton = Button(win, text='-', width=4, command=lambda: set_text('-'), fg='black', bg='light green')
dividebutton = Button(win, text='/', width=4, command=lambda: set_text('/'), fg='black', bg='light green')
backspacebutton = Button(win, text='⌫', width=4, font='Helvetica 8', command=lambda: clear1(), fg='black',
                         bg='light green')
equalbutton = Button(win, text='=', width=4, command=lambda: equate(), fg='black', bg='light green')
pointbutton = Button(win, text='.', width=4, command=lambda: set_text('.'), fg='black', bg='light green')
reminderbutton = Button(win, text='%', width=4, command=lambda: set_text('%'), fg='black', bg='light green')
# show arithmetic button
plusbutton.grid(row=3, column=3, stick='e')
mulbutton.grid(row=4, column=3, stick='e')
minusbutton.grid(row=5, column=3, stick='e')
dividebutton.grid(row=6, column=3, stick='e')
backspacebutton.grid(row=3, column=2, stick='e')
equalbutton.grid(row=7, column=3, stick='e')
pointbutton.grid(row=7, column=1, stick='e')
reminderbutton.grid(row=7, column=2, stick='e')
# clear buttons
clearbutton = Button(win, text='C', width=4, command=lambda: clearall(), fg='black', bg='light green').grid(row=3,
                                                                                                            column=0,
                                                                                                            stick='e')
cebutton = Button(win, text='CE', width=4, command=lambda: clearall(), fg='black', bg='light green').grid(row=3,
                                                                                                          column=1,
                                                                                                          stick='e')


def set_text(text):
    result.insert(END, text)


def clearall():
    result.delete(0, END)


def clear1():
    txt = result.get()[:-1]
    result.delete(0, END)
    result.insert(0, txt)


def equate():
    error = 'INVALID SYNTAX'
    try:
        value = eval(result.get())
    except SyntaxError:
        result.delete(0, END)
        result.insert(0, error)
    else:
        result.delete(0, END)
        result.insert(0, value)

def enter(event):
    equate()


result.bind('<Return>',enter)


win.mainloop()
