print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_percent = 1 + int(tip)/100
people = int(input("How many people to split the bill? "))
each_person_pay = round(bill * bill_percent/people, 2)
print (f"Each person should pay: ${each_person_pay}")