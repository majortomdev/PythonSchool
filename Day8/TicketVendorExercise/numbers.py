def decorate_get_ticket(ticket_chosen):

        print("Your number is ")
        if ticket_chosen == 'P':
            print(next(p))
        elif ticket_chosen == 'M':
            print(next(m))
        else:
            print(next(c))
        print("Please wait, you will be seen to soon")



#@decorate_get_ticket
def get_perfume_ticket():
    pticket = 0
    while True:
        pticket += 1
        yield "P-"+str(pticket)

#@decorate_get_ticket
def get_medicine_ticket():
    mticket = 0
    while True:
        mticket += 1
        yield "M-" + str(mticket)

#@decorate_get_ticket
def get_cosmetic_ticket():
    cticket = 0
    while True:
        cticket += 1
        yield "C-"+str(cticket)









#@decorate_get_ticket
# def get_perfume_ticket():
#     for n in range(1,10000):
#         yield f'P - {n}'
#
# #@decorate_get_ticket
# def get_medicine_ticket():
#     for n in range(1,10000):
#         yield f'M - {n}'
#
# #@decorate_get_ticket
# def get_cosmetic_ticket():
#     for n in range(1,10000):
#         yield f'C - {n}'


p = get_perfume_ticket()
m = get_medicine_ticket()
c = get_cosmetic_ticket()
