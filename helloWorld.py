import datetime

# my first python programme
print("hello world")

today = datetime.datetime.today()

dayOfWeek = today.weekday()

if dayOfWeek == 1:
    print("It's Tuesday")
elif dayOfWeek == 2:
    print("It's Wednesday")
else:
    print("It's not Tuesday")
