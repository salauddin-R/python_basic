temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

scorse = 75
if scorse>=90:
    print("Grade A++")
elif scorse>=80:
    print("Grade:A+")
elif scorse>=70:
    print("Grade: B")
else:
    print("you are fail")    

a=90
b=100
c=a if a>b else b
print("c = ",c)

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

value = 0
if value < 0:
  print("Negative value")
elif value == 0:
  pass #not do any thing
else:
  print("Positive value")

month = 4
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

for i in range(2,100,10):
    if i==12:
      continue
    print(i)