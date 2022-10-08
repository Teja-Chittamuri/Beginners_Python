# In Python inorder to execute for loop we need to use --- range (start, stop, Increment value)

#  for(x=1, x<10, x++)  ----- similar to this
# for x in range(1, 10, 2):   ---------Mainly helpful when we tp print sequence of numbers
#      print('value of X:', x)

# fruits = ['🍎', '🍌','🍉','🍓','🍍','🍊']   -------- Mainly helpful when we want to print a list or Array elem individually.
# for y in fruits:
#   print(y)
# ======================================================================================================================================

# Nested  While loop
# IMP if we miss any of these that will cause the loop remains running which crashes the program
# 1. Need to create a variable to count the iteration
# 2. specify the condition in while loop
# 3. specify the incrementation


# i = 1
#
# while i < 5:
#  print("Teja", end=" ")
#
#
#  j = 1
#  while j < 4:
#    print("Rocks", end="\t")
#    j = j + 1
#
#  i = i + 1
#  print()



# bio= ['Teja','microsoft',78]
# bio = 'My name is Teja Chittamuri'
#
# for x in bio:
#  print(x)
#
#  i = 1
#  while i < 10 :
#   print(i)
#   i = i + 1

# ==================================================================================================================

# num1 = int(input("enter 1st value\n"))
# num2 = int(input("enter  2nd value\n"))
# # sum = num1 + num2
# # print(f"The sum of two numbers is {sum}")
#
# def sum_of_numbers (x,y):
#     return f"The sum of two numbers is {x + y}"
#
# print(sum_of_numbers(num1,num2))

# =============================================================================================================

# Tip Calculator app ----- which covers the basic concepts

# food_amount = int(input("Tell me your ordered food amount?\n"))
# tip = int(input("Enter tip amount \n"))
# def tip_calc(x):
#   tip_percent = food_amount * (tip / 100)
#   #  tip_percent = food_amount * tip
#   print('-----------------------------------')
#   total_bill = food_amount + tip_percent
#   print(f"your ordered 🍟🍗food price is 💰${food_amount}")
#   print(f"The tip amount is 💰${tip_percent}")
#   print(f"Total amount is 💰${total_bill}")
# print(tip_calc(food_amount))

# ================================================================================================================


#  Baby weather app  ------ which covers the If else If loops
#
# weather_condition = input("what is the weather condition now? \n")
# if weather_condition == "Rainy":
#   print("Hey carry an umbrella that keeps you way from the Rain☔")
# elif weather_condition == "Sunny":
#   print("Hey Grab your SunGlasses & Apply Sunscreen🕶️")
# elif weather_condition == "Thundery":
#   print("Hey It is Thundering Don't go to outside⛈")
# else:
#   print("Hey the weather looks Good all set to go out & chill🍹!")


# Score card & grading ------ which covers the If else If loops & logical operators

# student_score = int(input("Enter your marks? \n"))
# if student_score >= 90:
#   print("You passed👍 : A Grade")
# elif student_score >= 80:
#   print("You passed👍 : B Grade")
# elif student_score >= 70:
#   print("You passed👍 : C Grade")
# elif student_score >= 60:
#   print("You passed👍 : D Grade")
# elif student_score == 60:
#   print("you passed👍 : F Grade")
# else:
#   print("You Failed👎 ! please try to clear it in supply😅")

# Normal way of writing if using logical operators
# if student_score <= 60 or student_score <= 90:
#   print('you passed in distinction')

# Pythonic way of writing and operator

# if 60 >= student_score <= 90:
#     print("You Passed")


#  ===================================================================================================================


# Functions

# name_input = input("Enter your name? \n")
# greet = "Good Morning"

#  Passing Arguments to print the output dynamically
#
# def say_myname(name,msg):
#     return f"Hello {msg} {name}"
#
#
# print(say_myname(name_input,greet))

#  Default Arguments
# In this example we are passing "Greet value as "Hello" by default which prints it by default even if we missed to call that argument

# def say_myname2(name,greet='Hello'):
#     return f"{greet} {name} "
#
# print(say_myname2(name_input))

# Adding 3 values using Functions

# value_1 = int(input("Enter the 1st value?\n"))
# value_2 = int(input("Enter the 2nd value?\n"))
# value_3 = int(input("Enter the 3rd value?\n"))
#

# TypeHinting helps to understand what type of data that the function is expecting
# Here in below ex the function can accept arguments type "INT" and returns "INT"

# def sum(a: int,  b: int, c: int) -> int:
#     return f"The sum of three values is {a+b+c}"

#
# print(sum(value_1, value_2, value_3))


# Tip Calculator Using Functions

# food_amount = int(input("Tell me your ordered food amount?\n"))
# tip = int(input("Enter tip amount \n"))
#
#
# def tip_calculator(amount, tip_percent):
#   tip_amount = amount * (tip_percent / 100)
#   print('======================================')
#   total_bill = amount + tip_amount
#   return f"The 🍟🍗Food amount is ${amount}💵 and the Tip amount is {tip_amount}💵.\nSo the Total Amount is ${total_bill}💵"
#
# print(tip_calculator(food_amount,tip))

# Weather Emoji app using functions

weather_input = input("What is the weather Condition Right Now? \n")

# TypeHinting helps to understand what type of data that the function is expecting

# Here in below ex
# "str" refers that the argument must be a string
# "None" refers what type of output it delivers in this case it is emoji's..


def weather_to_emoji(usr_input: str) -> None:
    if usr_input == "rainy":
        print('☂️☂️☂️☂️')
    elif usr_input == "thunderstorm":
        print("⛈️⛈️⛈️")
    elif usr_input == "sunny":
        print("🧴🧴🧴🕶️🕶️🕶️")

weather_to_emoji(weather_input)

