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
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg= 'azure4', padx= 50)
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
food_box=[]
food_text=[]
counter = 0
for food in food_list:

    # CREATE Checkbuttons
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text = food.title(),
                       font = ('Dosis',19,'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable= food_variables[counter])
    food.grid(row= counter,
              column= 0,
              sticky= W)

    # CREATE input boxes
    food_box.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_box[counter] = Entry(food_panel,
                              font= ('Dodis',18,'bold'),
                              bd=1,
                              width=6,
                              state= DISABLED,
                              textvariable= food_text[counter])
    food_box[counter].grid(row=counter,
                           column= 1)

    counter +=1

# create DRINK ITEMS
drink_variables = []
drink_box=[]
drink_text=[]
counter = 0
for drink in drink_list:

    # CREATE Checkbuttons
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel,
                        text=drink.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=drink_variables[counter])
    drink.grid(row=counter,
               column=0,
               sticky=W)

    # CREATE input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter] = Entry(drink_panel,
                              font= ('Dodis',18,'bold'),
                              bd=1,
                              width=6,
                              state= DISABLED,
                              textvariable= drink_text[counter])
    drink_box[counter].grid(row=counter,
                           column= 1)

    counter += 1

# create DESSERT ITEMS
dessert_variables = []
dessert_box=[]
dessert_text=[]
counter = 0
for dessert in dessert_list:

    # CREATE Checkbuttons
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text=dessert.title(),
                          font= ('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_variables[counter])
    dessert.grid(row=counter,
                 column=0,
                 sticky=W)

    # CREATE input boxes
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter] = Entry(dessert_panel,
                              font= ('Dodis',18,'bold'),
                              bd=1,
                              width=6,
                              state= DISABLED,
                              textvariable= dessert_text[counter])
    dessert_box[counter].grid(row=counter,
                           column= 1)

    counter += 1


# VARIABLES
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

# COST labels and input fields
food_cost_label = Label(cost_panel,
                        text='Food Cost',
                        font= ('Dosis',12,'bold'),
                        bg= 'azure4',
                        fg = 'white')
food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(cost_panel,
                       font= ('Dosis',12,'bold'),
                       bd=1,
                       width= 10,
                       state= 'readonly',
                       textvariable= food_cost_var)
food_cost_text.grid(row =0, column= 1, padx=41)

drink_cost_label = Label(cost_panel,
                        text='Drink Cost',
                        font= ('Dosis',12,'bold'),
                        bg= 'azure4',
                        fg = 'white')
drink_cost_label.grid(row=1, column=0)
drink_cost_text = Entry(cost_panel,
                       font= ('Dosis',12,'bold'),
                       bd=1,
                       width= 10,
                       state= 'readonly',
                       textvariable= drink_cost_var)
drink_cost_text.grid(row =1, column= 1)

dessert_cost_label = Label(cost_panel,
                        text='Dessert Cost',
                        font= ('Dosis',12,'bold'),
                        bg= 'azure4',
                        fg = 'white')
dessert_cost_label.grid(row=2, column=0)
dessert_cost_text = Entry(cost_panel,
                       font= ('Dosis',12,'bold'),
                       bd=1,
                       width= 10,
                       state= 'readonly',
                       textvariable= dessert_cost_var)
dessert_cost_text.grid(row =2, column= 1)

subtotal_label = Label(cost_panel,
                        text='Subtotal',
                        font= ('Dosis',12,'bold'),
                        bg= 'azure4',
                        fg = 'white')
subtotal_label.grid(row=0, column=2)
subtotal_text = Entry(cost_panel,
                       font= ('Dosis',12,'bold'),
                       bd=1,
                       width= 10,
                       state= 'readonly',
                       textvariable= subtotal_var)
subtotal_text.grid(row =0, column= 3)

taxes_label = Label(cost_panel,
                        text='Taxes',
                        font= ('Dosis',12,'bold'),
                        bg= 'azure4',
                        fg = 'white')
taxes_label.grid(row=1, column=2)
taxes_text = Entry(cost_panel,
                       font= ('Dosis',12,'bold'),
                       bd=1,
                       width= 10,
                       state= 'readonly',
                       textvariable= taxes_var)
taxes_text.grid(row =1, column= 3)

total_label = Label(cost_panel,
                        text='Total',
                        font= ('Dosis',12,'bold'),
                        bg= 'azure4',
                        fg = 'white')
total_label.grid(row=2, column=2)
total_text = Entry(cost_panel,
                       font= ('Dosis',12,'bold'),
                       bd=1,
                       width= 10,
                       state= 'readonly',
                       textvariable= total_var)
total_text.grid(row =2, column= 3)


# prevent WINDOW from closing
application.mainloop()
