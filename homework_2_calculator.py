# Simple Calculator exercise

# define to add two numbers
def add (num1, num2):
    return num1 + num2

# define to subract two numbers
def subtract(num1, num2):
    return num1 - num2

# define to multiply two numbers
def multiply (num1, num2):
    return num1 * num2

# define to divide two numbers
def divide (num1, num2):
    return num1 / num2

# Made the program a little interactive using some prints
print ("Welcome to your calculator!" )
print ("Select your calculator operator -\n"
      "1 - Add\n"\
      "2 - Subtract\n"\
      "3 - Multiply\n"\
      "4 - Divide\n")


# Takes in user input
pick = input("Please select the operator from 1, 2, 3, 4: ")

value1= float(input('Enter your first value: '))
value2 = float(input('Enter your second value: '))

if pick =='1':
    print(value1, "+", value2 , "=", add(value1, value2))

elif pick == '2':
    print(value1, "-", value2 , "=",
          subtract(value1, value2))

elif pick =='3':
    print(value1, "*", value2 , "=",
          multiply(value1, value2))

elif pick =='4':
    print(value1, "/", value2 , "=",
          divide(value1, value2))
else:
    print("Invalid input")
