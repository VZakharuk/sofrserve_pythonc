def math_symb_l(key):
    if key == "+":
        str_2 = "-+.*/"
        if "+" in calc_entry.get():
            for key in str_2:
                if key.count(key) > 1:
                    key = key.replace(key, "", key.count(key)-1)
            calc_entry.insert(0)
        # calc_entry.delete(0)


from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry('368x428+950+50')

root.resizable(False, False)

root.title("Calculator")


def calc(key):
    # logic of calculator
    global memory
    if key == "=":

        # exclude writing letters
        str_1 = "-+0123456789.*/"
        if calc_entry.get()[0] not in str_1:
            calc_entry.insert(END, "=" + "Error")
            messagebox.showerror("Error!", "The first symbol is not number!")

        # calculation
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "=" + "Error!")
            messagebox.showerror("Error", "Make sure the data is entered correctly")

    elif key == "+":
        if "+" in calc_entry.get():
            if calc_entry.count("+") > 1:
                calc_entry.replace("+", "", calc_entry.count("+")-1)
            calc_entry.insert(0, "+")
        calc_entry.insert(END, "+")

    # clearing the field of entry
    elif key == "AC":
        calc_entry.delete(0, END)

    # change "-" to "+" and back
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# Create all button
button_list = [
    "AC", "/", "*", "-/+",
    "7", "8", "9", "-",
    "4", "5", "6", "+",
    "1", "2", "3", "",
    "0", ".", " ()", "="
]
r = 1  # row
c = 0  # column

for i in button_list:
    rel = ""
    calc_cmd = lambda x = i: calc(x)

    Button(root, text=i, width=8, height=4, command=calc_cmd).grid(row=r, column=c)
    c += 1
    if c >= 4:
        c = 0
        r += 1

# create field of entry
calc_entry = Entry(root, width=36)
calc_entry.grid(row=0, column=0, columnspan=4)


root.mainloop()

###########################################################################

# from tkinter import *
#
#
# def insertText():
#     s = "Hello World"
#     text.insert(1.0, s)
#
#
# def getText():
#     s = text.get(1.0, END)
#     label['text'] = s
#
#
# def deleteText():
#     text.delete(1.0, END)
#
#
# root = Tk()
#
# text = Text(width=25, height=5)
# text.pack()
#
# frame = Frame()
# frame.pack()
#
# b_insert = Button(frame, text="Вставить", command=insertText)
# b_insert.pack(side=LEFT)
#
# b_get = Button(frame, text="Взять", command=getText)
# b_get.pack(side=LEFT)
#
# b_delete = Button(frame, text="Удалить", command=deleteText)
# b_delete.pack(side=LEFT)
#
# label = Label()
# label.pack()
#
# root.mainloop()

######################################################################

# from tkinter import *
#
# def take():
#     l['text'] = "Выдано"
#
#
# root = Tk()
# Label(text="Пункт выдачи").pack()
# Button(text="Взять", command=take).pack()
# l = Label(width=10, height=1)
# l.pack()
# root.mainloop()


