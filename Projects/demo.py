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
# firstName = "Chittamuri"
# lastName = "Teja"
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

# Tip Calculator If-else

# bill_amount = int(input("Enter your bill amount? \n"))
#
# if bill_amount > 1000:
#     tip = bill_amount * 0.3
# else:
#     tip = bill_amount * 0.1
#
# total_bill = bill_amount + tip
#
# def tip_cal(x,y,z):
#
#     return f"Hi sir ,your Bill amount is ${x} and the tip amount is ${y}.so the total bill amount is {z}"
#
# print(tip_cal(bill_amount,tip,total_bill))

# Type casting  changing the type of the data from one data type to another

# In python type() is used to  verify the datatype

# is_playing = [1, 'tej', 2.5]
# print(type(is_playing))

# Program that specifies the concepts of functions , if else loops, nested loops & Typeconvesrion & Maintaing a clean code
#Always try to encapsulate the program logic inside a function which keeps our code cleaner and maintable

# def time_calculator(no_of_days):
#     return f"{no_of_days} days are equal to {no_of_days * timeInHours} Hours"

# def validate_and_execute():
#   if user_input.isdigit():
#      input_number = int(user_input)
#      if input_number > 0:
#        return time_calculator(input_number)
#   elif user_input == 0:
#               return "you entered zero which is not at all a valid one!Please enter a valid number!"
#   else:
#             return "You Entered an Invalid Text. Please enter a valid number!"

# In Python "try" --- helps to ran a  block of code
# "except" -- if the exceution stopped because of any kind of errors then it collects that error and print some message to the user.


# def validate_and_execute():
#     try:
#         input_number = int(user_input)
#         if input_number > 0:
#             return time_calculator(input_number)
#         elif user_input == 0:
#          return "you entered zero which is not at all a valid one!Please enter a valid number!"
#         else:
#             return "you entered a negative number which is not supported for conversion.please enter a positive number!"
#     except:
#       print("You Entered an Invalid Text. Please enter a valid number!")
#
# user_input = ""
# while user_input != "exit":
#  user_input = input("Hey user enter no.of days? \n")
#  print(validate_and_execute())

# List datatype similar as Array
# Here in this program we are using for loop to repeat the same task for certain elements in the list.

# def time_calculator(no_of_days):
#     return f"{no_of_days} days are equal to {no_of_days * timeInHours} Hours"
# def validate_and_execute():
#     try:
#         input_number = int(num_of_days)
#         if input_number > 0:
#             return time_calculator(input_number)
#         elif user_input == 0:
#          return "you entered zero which is not at all a valid one!Please enter a valid number!"
#         else:
#             return "you entered a negative number which is not supported for conversion.please enter a positive number!"
#     except:
#       print("You Entered an Invalid Text. Please enter a valid number!")
#
# user_input = ""
# while user_input != "exit":
#  user_input = input("Hey user enter no.of days? \n")
#  for num_of_days in user_input.split():
#   print(validate_and_execute())








