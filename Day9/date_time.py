# import datetime
#
# my_time = datetime.time(17, 35)
# print(type(my_time))
#
# my_day = datetime.date(2025, 10, 17)
# print(my_day)



###*******************************


from datetime import datetime
from datetime import date

my_date = datetime(2025,5,15,22,10,15,2500)
print(my_date)



birth = date(1995, 3 ,5)

death = date(2095, 3 ,3)

life = death - birth

print(str(life.days/365) + " years old")


current_minutes = datetime.now().minute

print(current_minutes)

