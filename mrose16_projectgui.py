# Miriam Rose CIS 345 online Final Project

from tkinter import *
from PIL import Image, ImageTk
from Class import Order
import time

# dictionaries to create multiple buttons
order_types = {'Pickup': 1, 'Delivery': 2}
values = list(order_types.values())
locations = {'Mesa: 22 South Mesa Drive': 'Mesa', 'Tempe: 1017 East Apache': 'Tempe',
             'Phoenix 1: 1111 East Buckeye': 'Phoenix 1', 'Phoenix 2: 2628 West Van Buren': 'Phoenix 2',
             'Phoenix 3: 3920 South Central': 'Phoenix 3', 'Phoenix 4: 4121 North 44th Street': 'Phoenix 4',
             'Glendale: 5516 Glendale Avenue': 'Glendale', 'Tolleson: 9309 West Van Buren': 'Tolleson'}

orders = []


def close():
    win.destroy()


def clear_checkboxes():
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    c6.deselect()
    c7.deselect()
    c8.deselect()


def rad_click():
    toggle_address(order_type.get())


def toggle_address(index):
    if index == 1:
        address_entry.config(state=DISABLED)
    else:
        address_entry.config(state=NORMAL)


def next1():
    order_frame.grid_forget()
    locations_frame.grid(columnspan=2)
    locations_frame.pack_propagate(False)


def back():
    locations_frame.grid_forget()
    order_frame.grid(columnspan=2)


def submit_button():
    global orders
    orders = [checkvar1.get(), checkvar2.get(), checkvar3.get(), checkvar4.get(),
              checkvar5.get(), checkvar6.get(), checkvar7.get(), checkvar8.get()]
    orders = list(filter(None, orders))

    new_order = Order(name_entry.get(), time.ctime(), address_entry.get(), order_type.get(), location.get(), orders)
    cost = new_order.add_order()

    total_lbl.config(text=f'Thank you {name_entry.get()}, Total cost is ${cost:.2f}!')
    clear_checkboxes()


# window creation
win = Tk()
win.title("Pete's Fish and Chips")
win.geometry('500x750')
win.config(bg='red')

# Variable
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
checkvar4 = IntVar()
checkvar5 = IntVar()
checkvar6 = IntVar()
checkvar7 = IntVar()
checkvar8 = IntVar()
name = StringVar()
address = StringVar()
order_type = IntVar()
location = StringVar(value='')

canvas = Canvas(win, width=450, height=190, bg='red')
canvas.grid(columnspan=2, pady=10)

# Add an image
logo = Image.open('fishandchips.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=2, column=0, row=0, pady=10)

# Order page
order_frame = Frame(win, width=360, height=500, bg='white')
order_frame.grid(columnspan=2)
order_frame.pack_propagate(False)

# Labels
shop_lbl = Label(order_frame, text="Welcome to Pete's Fish and Chips", width=30, bg='black',
                 font=('Arial', 20), fg='white')
shop_lbl.grid(columnspan=2, row=1)

info_lbl = Label(order_frame, text='Menu: Please select your items', width=30, bg='black',
                 font=('Arial', 17), fg='white')
info_lbl.grid(columnspan=2, row=2, pady=5)

# Frame for checkboxes
box1 = Frame(order_frame, bg='white', width=400, height=120, borderwidth=5, relief=RIDGE)
box1.grid(row=3, column=0, columnspan=2)
box1.grid_propagate(False)
box1.columnconfigure(0, weight=1)
box1.columnconfigure(1, weight=1)

# Checkboxes
c1 = Checkbutton(box1, text="Fish and Chips...........$8.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar1,
                 font=("Arial", 11), onvalue=1, offvalue=0)
c1.grid(row=1, column=0, sticky=W)

c2 = Checkbutton(box1, text="Shrimp and Chips.....$10.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar2,
                 font=("Arial", 11), onvalue=2, offvalue=0)
c2.grid(row=2, column=0, sticky=W)

c3 = Checkbutton(box1, text="Crab and Chips........$10.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar3,
                 font=("Arial", 11), onvalue=3, offvalue=0)
c3.grid(row=3, column=0, sticky=W)

c4 = Checkbutton(box1, text="Chicken Tenders........$7.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar4,
                 font=("Arial", 11), onvalue=4, offvalue=0)
c4.grid(row=4, column=0, sticky=W)

c5 = Checkbutton(box1, text="Seafood Combo....$8.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar5,
                 font=("Arial", 11), onvalue=5, offvalue=0)
c5.grid(row=1, column=2, sticky=W)

c6 = Checkbutton(box1, text="Monster Burger.....$9.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar6,
                 font=("Arial", 11), onvalue=6, offvalue=0)
c6.grid(row=2, column=2, sticky=W)

c7 = Checkbutton(box1, text="Hot Dog.................$5.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar7,
                 font=("Arial", 11), onvalue=7, offvalue=0)
c7.grid(row=3, column=2, sticky=W)

c8 = Checkbutton(box1, text="Fish Sandwich......$4.00", fg='#6f4e37', bg='white', bd=2, variable=checkvar8,
                 font=("Arial", 11), onvalue=8, offvalue=0)
c8.grid(row=4, column=2, sticky=W)

# Entry box
order_lbl = Label(order_frame, text='Pickup or Delivery ', width=30, bg='black',
                  font=('Arial', 17), fg='white')
order_lbl.grid(columnspan=2, column=0, row=4, pady=5)

# Radio buttons
box2 = Frame(order_frame, bg='white', width=400, height=120, borderwidth=5, relief=RIDGE)
box2.grid(row=5, column=0, columnspan=2)
box2.grid_propagate(False)
box2.columnconfigure(0, weight=1)
box2.columnconfigure(1, weight=1)

for (text, value) in order_types.items():
    Radiobutton(box2, text=text, value=value,
                variable=order_type, anchor=S, width=15, font=1,
                bg='white',
                command=rad_click).pack(fill=X, padx=5, side=LEFT,
                                        ipadx=0, ipady=0)

# Name and address entry
name_lbl = Label(order_frame, text='Enter Name: ', bg='white', font=12)
name_lbl.grid(row=6, column=0, ipadx=10, padx=10, sticky=E)
name_entry = Entry(order_frame, textvariable=name, width=40)
name_entry.grid(row=6, column=1, pady=10, sticky=W)

address_lbl = Label(order_frame, text='Enter Address: ', bg='white', font=12)
address_lbl.grid(row=7, column=0, ipadx=10, padx=10, sticky=E)
address_entry = Entry(order_frame, textvariable=address, width=40)
address_entry.grid(row=7, column=1, pady=10, sticky=W)

# Buttons
next_button = Button(order_frame, command=next1,
                     font=("Arial", 16), text='Next', width=12)
next_button.grid(column=0, row=10, pady=(20, 10), padx=(30, 0), sticky=E)

exit_button = Button(order_frame, command=close,
                     font=("Arial", 16), text='Exit', width=12)
exit_button.grid(column=1, row=10, pady=(20, 10), padx=(30, 0), sticky=W)

# locations page
locations_frame = Frame(win, width=360, height=500, bg='white')

restaurants_lbl = Label(locations_frame, text="Restaurant locations", width=30, bg='black',
                        font=('Arial', 20), fg='white')
restaurants_lbl.grid(columnspan=2, row=0)

restaurants2_lbl = Label(locations_frame, text="All locations open from 10AM - 10PM, Mon - Sat", width=40, bg='black',
                         font=('Arial', 16), fg='white')
restaurants2_lbl.grid(columnspan=2, row=1)

restaurants3_lbl = Label(locations_frame, text="Please choose a restaurant for your order: ", width=40, bg='black',
                         font=('Arial', 16), fg='white')
restaurants3_lbl.grid(columnspan=2, row=2)

# Radio buttons for locations
box3 = Frame(locations_frame, bg='white', width=400, height=120, borderwidth=5, relief=RIDGE)
box3.grid(row=3, column=0, columnspan=2)

for (text, value) in locations.items():
    Radiobutton(box3, text=text, value=value,
                variable=location, anchor=W, width=40,
                bg='light yellow', font=5,
                command=rad_click).pack(fill=X, padx=1,
                                        ipadx=0, ipady=0)

submit_button = Button(locations_frame, command=submit_button,
                       font=("Arial", 16), text='Submit', width=15)
submit_button.grid(column=0, row=4, columnspan=2)

# Total cost label
total_lbl = Label(locations_frame, text='Hello!', width=45, bg='linen',
                  font=('Arial', 11))
total_lbl.grid(columnspan=2, column=0, row=5, pady=10)

# Buttons
back_button = Button(locations_frame, command=back,
                     font=("Arial", 16), text='Back', width=12)
back_button.grid(column=0, row=6, pady=(10, 10), padx=(30, 0), sticky=E)

exit_button = Button(locations_frame, command=close,
                     font=("Arial", 16), text='Exit', width=12)
exit_button.grid(column=1, row=6, pady=(10, 10), padx=(30, 0), sticky=W)

win.mainloop()
