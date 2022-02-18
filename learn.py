num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")
a = str(123)

print(type(a))# fstring
score = 0
height = 1.8
iswinning = True
print(f"your score is {score}, your height is {height},your winning is {iswinning}")

# Coding Exercise
number = input("Type a two digit number: ")
result =int(number[0])+int(number[1])
print(result)

# Coding exercise
# BMI =weight(kg)/height**2(m2)
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = float(weight)/float(height)**2
round_bmi = round(bmi,2)
print(round_bmi)

# Coding Exercise
# A year has 12 months, 52 weeks, 365 days
age = input("What is your current age?")
rem_yrs = 90-int(age)
rem_mnths =rem_yrs *12
rem_wks = rem_yrs*52
rem_days =rem_yrs*365
print(f"You have {rem_yrs} years,{rem_mnths} months,{rem_wks} weeks,{rem_days} days")
