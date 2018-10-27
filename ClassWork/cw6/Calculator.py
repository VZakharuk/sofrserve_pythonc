from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calculator")

#  calculator logic
def calc(key):
    global memory
    if key == "=":
#  exclude writing letters
        str_1 = "-+0123456789.*/"
        if calc_entry.get()[0] not in str_1:
            calc_entry.insert(END, "The first symbol is not number!")
            messagebox.showerror("Error!", "You input not number!")
# calculation
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Make sure the data is entered correctly")
# clearing the field
    elif key == "C":
        calc_entry.delete(0, END)
# change "-" to "+"
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "-" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# Create all button
button_list = [
    "C", "/", "*", "AC",
    "7", "8", "9", "-",
    "4", "5", "6", "+",
    "1", "2", "3", "-/+",
    "0", ".", " ", "="
]
r = 1  # row
c = 0  # column

for i in button_list:
    rel = ""
    cmd = lambda x = i: calc(x)
    ttk.Button(root, text=i, command = cmd).grid(row=r, column=c)
    c += 1
    if c >= 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=4)

root.mainloop()
