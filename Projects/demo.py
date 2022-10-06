# print('Hello World')

# Number DataType in Python
#
# num1 = 10
# num2 = 20
# num3 = 12.5
# num4 = num1 + num2 + num3
# print(num4)


# String concatenation
timeInHours = 24
timeInMinutes = 24 * 60
timeInSeconds = 24 * 60 * 60
# myString1 = f"30 days are equal to {30 * timeInMinutes} minutes"
# myString2 = f"30 days are equal to {30 * timeInSeconds} seconds"
# print(myString1)
# print(myString2)
#
firstName = "Chittamuri"
lastName = "Teja"
# print(firstName + lastName)

#  Functions
# Functions are blocks of codes which primarly used to avoid repetation of code and maintain it dynamically.
# In python Def is a keyword that tells that to tells to complier this is a function

#
# def time_calculator(no_of_days):
#     print(f"{no_of_days} days are equal to {no_of_days * timeInHours} Hours")
#     print(f"{no_of_days} days are equal to {no_of_days * timeInMinutes} Minutes")
#     print(f"{no_of_days} days are equal to {no_of_days * timeInSeconds} Seconds")
#
# print(time_calculator(20))



# Scope
# Global variables --- Accessible from all over the code & functions
# Local variables  -- Variables declared within the function can be accessible within the function and not accessible outside the function


# Taking from the user using input()

# birth_year = int(input("Hey user Enter your Birth year? \n"))
# age = 2022 - birth_year;
#
#
# def age_calculator(x):
#     print(f"{firstName} {lastName} is {x} years old")
#
#
# print(age_calculator(age))

# Tip Calculator

bill_amount = int(input("Enter your bill amount? \n"))

if bill_amount > 1000:
    tip = bill_amount * 0.3
else:
    tip = bill_amount * 0.1

total_bill = bill_amount + tip

def tip_cal(x,y,z):

    return f"Hi sir ,your Bill amount is ${x} and the tip amount is ${y}.so the total bill amount is {z}"

print(tip_cal(bill_amount,tip,total_bill))

