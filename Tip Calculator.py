# print a greeting
# Ask the user to input the total bill
# Ask the user to input the percentage of the tip from
# Ask the user to input the number of people paying
# Ask the user to input the number of people paying
# print what each person will pay
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12,or 15?"))
people_paying = int(input("How many people to split the bill?"))
money_paid = round(total_bill + ((tip / 100) * total_bill),2)
# money_paid= "{:.2f}".format(total_bill/people_paying,2)
print(f"Each person should pay: ${money_paid}")
