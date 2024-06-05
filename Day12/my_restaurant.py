from tkinter import *

operator = ''
food_price = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_price = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_price = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_button(character):
    global operator
    operator = operator + character
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)

def delete_all():
    global operator
    operator = ''
    calculator_display.delete(0 , END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)

def review_check():
    x = 0
    for b in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state=NORMAL)
            if food_box[x].get() == '0':
                food_box[x].delete(0, END)
            food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1

    x = 0
    for b in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=NORMAL)
            if drink_box[x].get() == '0':
                drink_box[x].delete(0, END)
            drink_box[x].focus()
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1

    x = 0
    for b in dessert_box:
        if dessert_variables[x].get() == 1:
            dessert_box[x].config(state=NORMAL)
            if dessert_box[x].get() == '0':
                dessert_box[x].delete(0, END)
            dessert_box[x].focus()
        else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1

def total_calculation():
    food_subtotal = 0
    p = 0
    for unit in food_text:
        food_subtotal = food_subtotal + (float(unit.get()) * food_price[p])
        p += 1

    drink_subtotal = 0
    p = 0
    for unit in food_text:
        drink_subtotal = drink_subtotal + (float(unit.get()) * drink_price[p])
        p += 1

    dessert_subtotal = 0
    p = 0
    for unit in food_text:
        dessert_subtotal = dessert_subtotal + (float(unit.get()) * dessert_price[p])
        p += 1

    my_subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    my_taxes = my_subtotal * 0.11
    my_total = my_subtotal + my_taxes

    food_cost_var.set(f'$ {round(food_subtotal, 2)}')
    drink_cost_var.set(f'$ {round(drink_subtotal, 2)}')
    dessert_cost_var.set(f'$ {round(dessert_subtotal, 2)}')
    subtotal_var.set(f'$ {round(my_subtotal, 2)}')
    taxes_var.set(f'$ {round(my_taxes, 2)}')
    total_var.set(f'$ {round(my_total, 2)}')

# INITIALISE TKinter
application = Tk()

application.title("My Restaurant - Billing System")
application.geometry('1135x630+0+0') # set window size was 1020x630
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
                       variable= food_variables[counter],
                       command= review_check)
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
                        variable=drink_variables[counter],
                        command= review_check)
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
                          variable=dessert_variables[counter],
                          command= review_check)
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

# BUTTONS
buttons = ['total', 'invoice','save','reset']
created_buttons = []
column = 0
for button in buttons:
    button = Button(button_panel,
                    text= button.title(),
                    font= ('Dosis', 14, 'bold'),
                    fg= 'white',
                    bg='azure4',
                    bd=1,
                    width=6,)#orig 9
    created_buttons.append(button)

    button.grid(row= 0,
                column= column)
    column +=1

created_buttons[0].config(command=total_calculation)

# INVOICE area
invoice_text = Text(invoice_panel,
                    font=('Dosis', 12, 'bold'),
                    height=10,
                    bd=1,
                    width=42
                    )
invoice_text.grid(row=0,
                  column=0)


# CALCULATOR
calculator_display = Entry(calculator_panel,
                           font=('Dosis', 12, 'bold'),
                           width=36,
                           bd=1)
calculator_display.grid(row=0, column=0, columnspan=4)

calculator_buttons= ['7', '8', '9', '+',
                     '4', '5', '6', '-',
                     '1', '2', '3', 'x',
                     'CE', 'Delete', '0', '/']

stored_buttons = []


my_row = 1
my_column = 0

for button in calculator_buttons:
    button = Button(calculator_panel,
                    text= button.title(),
                    fg= 'white',
                    bg= 'azure4',
                    bd=1,
                    width=8)

    stored_buttons.append(button)

    button.grid(row= my_row,
                column = my_column)

    if my_column == 3:
        my_row+=1

    my_column+=1

    if my_column == 4:
        my_column = 0


stored_buttons[0].config(command=lambda: click_button('7'))
stored_buttons[1].config(command=lambda: click_button('8'))
stored_buttons[2].config(command=lambda: click_button('9'))
stored_buttons[3].config(command=lambda: click_button('+'))
stored_buttons[4].config(command=lambda: click_button('4'))
stored_buttons[5].config(command=lambda: click_button('5'))
stored_buttons[6].config(command=lambda: click_button('6'))
stored_buttons[7].config(command=lambda: click_button('-'))
stored_buttons[8].config(command=lambda: click_button('1'))
stored_buttons[9].config(command=lambda: click_button('2'))
stored_buttons[10].config(command=lambda: click_button('3'))
stored_buttons[11].config(command=lambda: click_button('*'))
stored_buttons[12].config(command=get_result)
stored_buttons[13].config(command=delete_all)
stored_buttons[14].config(command=lambda: click_button('0'))
stored_buttons[15].config(command=lambda: click_button('/'))


# prevent WINDOW from closing
application.mainloop()
