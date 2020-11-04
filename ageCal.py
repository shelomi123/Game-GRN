from datetime import date

byear=input("Enter your birth year ex: 1995")
bmonth=input("Enter your birth month ex:05")
bday=input("Enter your birth day ex:23")

print('Birthday is', (bday+"/"+bmonth+"/"+byear))

today= date.today()

age=today.year - int(byear)

print(age)