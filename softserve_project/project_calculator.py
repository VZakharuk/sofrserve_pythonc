""""
Vasyl Zakharuk
Python Core 355
Project - Calculator
"""


from tkinter import *
from tkinter import messagebox
import math

# create the window
root = Tk()

root.geometry('272x412+950+30')

root.resizable(False, False)

root.title("Calculator")


# logic of calculator
def calc(key):
    # global memory
    if key == "=":

        # exclude writing letters
        str_1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str_1:
            calc_entry.insert(END, "=" + "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

        # calculation
        try:
            calc_result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(calc_result))
        except:
            calc_entry.insert(END, "=" + "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")

    # clearing the field of entry
    elif key == "AC":
        calc_entry.delete(0, END)

    # changing "-" to "+" and back
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    # mathematical constants and functions
    elif key == "sin":
        calc_entry.insert(0, str(math.sin(float(calc_entry.get()))))

    elif key == "cos":
        calc_entry.insert(0, str(math.cos(float(calc_entry.get()))))

    elif key == "xⁿ":
        calc_entry.insert(END, "**")

    elif key == "n!":
        if "n!" in calc_entry.get() is not int():
            calc_entry.delete(0)
        try:
            calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
        except ValueError:
            calc_entry.insert(END, "=" + "Error!")
            messagebox.showerror("Error!", "Number must be integer")
    elif key == "√":
        calc_entry.insert(END, "=" + str(math.sqrt(float(calc_entry.get()))))

    elif key == "π":
        calc_entry.insert(END, math.pi)

    elif key == "exp":
        calc_entry.insert(0, str(math.exp(float(calc_entry.get()))))

    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")

    # making a button for exit
    elif key == "Exit":
        messagebox.showinfo("Bye", "Thank oyu for watching!")
        root.after(1, root.destroy)

    else:

        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# Create a list of buttons
button_list = [
    "sin", "cos", "xⁿ", "n!",
    "AC",   "√",  "π",  "exp",
    "7",   "8",   "9",  "+",
    "4",   "5",   "6",  "-",
    "1",   "2",   "3",  "*",
    "0",   ".",   "±",  "/",
    "Exit", "(",   ")", "=",
]
# create buttons
r = 1  # row
c = 0  # column

for i in button_list:
    rel_button_list = ""
    calc_cmd = lambda x = i:  calc(x)

    Button(root, text=i, width=5, height=3, command=calc_cmd).grid(row=r, column=c)
    c += 1
    if c >= 4:
        c = 0
        r += 1

# create field of entry
calc_entry = Entry(root, width=32)
calc_entry.grid(row=0, column=0, columnspan=4)

root.mainloop()
