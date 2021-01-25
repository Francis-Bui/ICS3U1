
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
    
#use 3 single quotes at the beginning and at the end of a block of
#lines you want to comment out
'''
if name == "John" or name == "Bob":
    print("Your name is either John or Bob.")
    
    temperature = float(input('What is the temperature? '))
    if temperature > 20:
        print('Wear shorts.')
    else:
        print('Wear long pants.')
    print('Go walk the dog.')
'''