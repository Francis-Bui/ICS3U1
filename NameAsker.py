# print a message to the Output window
print("Heeey Celtics!")

# print a blank line
print()

# declare a variable... automatically determined by data type
age = 16
# print the variable (integer)
print(age)

# print the variable (decimal or "float")
temperature = 22.7
print ("Temp is %f" % temperature)

# if statement...
age = 15
if age == 15:
    # indented four spaces
    print("you are 15")

# boolean variables

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = str(input('What is your name?'))

age = int(input('What is your age?'))

print(f"Your name is {name} and your age is {age}")
