
# Need to calc the time in hours or minutes or sec based on the user input
# Declaring variables
time_in_hours = 24
time_in_minutes = 24 * 60
time_in_seconds = 24 * 60 * 60

# Function to count the total time in hours
def time_counter(num_of_days):
    return f"{num_of_days} Days is equal to {num_of_days * time_in_hours} Hours"

# Function to validate the conditions
def validate_execute():
 try:
  if user_input > 0:
    print(time_counter(user_input))
  elif user_input == 0:
    print("Hey user you entered 0 which is not at all supported for conversion")
 except:
    print("The number you entered is Invalid!Please enter a valid number")

user_input = ""
while user_input != "exit":
     user_input = int(input("Hey user please Enter a Number! \n"))
     print(validate_execute())

