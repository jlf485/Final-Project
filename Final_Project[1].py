from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

FOS = Tk()
FOS.geometry("600x500")
FOS.title("Food Ordering System")

item_label = Label(FOS, text="What kind of sandwich would you like?")
item_label.grid(row=0, column=0)

item_entry = Entry(FOS, width=30)
item_entry.grid(row=0, column=1)

account_label = Label(FOS, text="Login or register account")
account_label.grid(row=1, column=0)

account_entry = Entry(FOS, width=30)
account_entry.grid(row=1, column=1)

ready_label = Label(FOS, text="Press at arrival")
ready_label.grid(row=2, column=0)

ready_entry = Entry(FOS, width=30)
ready_entry.grid(row=2, column=1)

# Create Sandwich list
my_Sandwich_list = ["Cheeseburger", "Hamburger", "Hot Dog", "Chicken Sandwich", "Ham Sandwich"]

Sandwich_list = Listbox(FOS, selectmode=MULTIPLE, bg="black", fg="white")
Sandwich_list.grid(row=4, column=1)

for item in my_Sandwich_list:
    Sandwich_list.insert(0, item)


def add_sandwich():
    result = ""
    for item in Sandwich_list.curselection():
        result = result + str(Sandwich_list.get(item)) + "\n"

        add_lbl.config(text="Your Selection: " + "\n" + result)


add_button = Button(FOS, text="Add Sandwich")
add_button.grid(row=5, column=0)


def check():
    text1 = name.entry.get()
    new_lbl = Label(FOS, text="Name: " + text1)
    new_lbl.grid(row=4, column=2)

    text2 = address_entry.get()
    new_lb2 = Label(FOS, text="Address: " + text2)
    new_lb2.grid(row=5, column=2)

    text3 = ready_entry.get()
    new_lb3 = Label(FOS, text="Ready: " + text3)
    new_lb3.grid(row=7, column=2)

check_button = Button(FOS, text="Checkout", command=check)
check_button.grid(row=6, column=0)


def delete():
    Sandwich_list.delete(0, 5)

del_button = Button(FOS, text="Remove Item", command=delete)
del_button.grid(row=7, column=0)


drinks = StringVar()
drinks.set("Choose a drink")

drink = OptionMenu(FOS, drinks, "Pepsi", "Mountain Dew", "Dr. Pepper", "Diet Pepsi")
drink.grid(row=8, column=0)


Sandwich_pic = ImageTk.PhotoImage(Image.open("sandwich.png"))
pic_lbl = Label(FOS, image=Sandwich_pic)
pic_lbl.grid(row=1, column=7)

drink_pic = ImageTk.PhotoImage(Image.open("drinks.jpg"))
pic_lbl = Label(FOS, image=drink_pic)
pic_lbl.grid(row=1, column=8)


def exit():
    answer = messagebox.askyesno("Hi", "Are you sure you want to exit?")
    if answer == 1:
        Sandwich.destroy()
    else:
        return


exit_button = Button(FOS, text="Exit", command=exit)
exit_button.grid(row=4, column=7)


FOS.mainloop()

