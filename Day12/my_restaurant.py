from tkinter import *

# INITIALISE TKinter
application = Tk()

application.title("My Restaurant - Billing System")
application.geometry('1020x630+0+0') # set window size
application.resizable(False, False)
application.config(bg='burlywood')


# TOP panel
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side= TOP)

# TITLE tag
title_tag = Label(top_panel, text= "Billing System", fg= 'azure4',
                  font= ('Dosis', 58), bg = 'burlywood', width= 27)
title_tag.grid(row=0, column=0)

# LEFT panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side= LEFT)

# COST panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT)
cost_panel.pack(side= BOTTOM)

# FOOD panel
food_panel = LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold'),
                        bd = 1, relief= FLAT, fg = 'azure4')
food_panel.pack(side=LEFT)

# DRINK panel
drink_panel = LabelFrame(left_panel, text='Drink', font=('Dosis', 19, 'bold'),
                        bd = 1, relief= FLAT, fg = 'azure4')
drink_panel.pack(side=LEFT)

# DESSERT panel
dessert_panel = LabelFrame(left_panel, text='Dessert', font=('Dosis', 19, 'bold'),
                        bd = 1, relief= FLAT, fg = 'azure4')
dessert_panel.pack(side=LEFT)

# RIGHT panel
right_panel = Frame(application, bd=1, relief= FLAT)
right_panel.pack(side= RIGHT)

# CALCULATOR panel
calculator_panel = Frame(right_panel, bd=1, relief= FLAT, bg='burlywood')
calculator_panel.pack()

# INVOICE panel
invoice_panel = Frame(right_panel, bd=1, relief= FLAT, bg='burlywood')
invoice_panel.pack()

# BUTTON panel
button_panel = Frame(right_panel, bd=1, relief= FLAT, bg='burlywood')
button_panel.pack()

# PRODUCT lists
food_list = ['Chicken','Salmon','Hake','Lamb','Donor Kebab','Pizza1','Pizza2','Pizza3']
drink_list = ['Lemonade', 'Soda', 'Juice', 'Cola', 'WineRed', 'WineWhite', 'Champagne','Beer']
dessert_list = ['Ice cream', 'Fruit', 'Brownies', 'Cheesecake', 'Banana bread', 'Pavlova', 'Mouse', 'Cream bun']

# create FOOD ITEMS
food_variables = []
counter = 0
for food in food_list:
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, text = food.title(), font = ('Dosis',19,'bold'),
                       onvalue=1, offvalue=0, variable= food_variables[counter])
    food.grid(row= counter, column= 0, sticky= W)
    counter +=1

# create DRINK ITEMS
drink_variables = []
counter = 0
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel, text=drink.title(), font=('Dosis', 19, 'bold'),
                       onvalue=1, offvalue=0, variable=drink_variables[counter])
    drink.grid(row=counter, column=0, sticky=W)
    counter += 1

# create DESSERT ITEMS
dessert_variables = []
counter = 0
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel, text=dessert.title(), font=('Dosis', 19, 'bold'),
                        onvalue=1, offvalue=0, variable=dessert_variables[counter])
    dessert.grid(row=counter, column=0, sticky=W)
    counter += 1


# prevent WINDOW from closing
application.mainloop()

