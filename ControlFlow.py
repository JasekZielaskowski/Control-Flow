
# Programmer: Jasek Zielaskowski
# Date: 12.16.19
# Program: Guess My Number



myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to myNumber
while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongratulations, you guessed my number!!!\n")



# Programmer: Jasek Zielaskowski
# Date: 12.19.19
# Program:1 - 10


x = 1

# While loop will see if a condition has been met
# If not is will run again until the condition
# has been met

while x <= 10:
    print(x)
    x+=1

# Programmer: Jasek Zielaskowski
# Date: 1.6.20
# Program: Running Total, Part II

# This program asks users for five numbers
# It then sums up the numbers

# Date: 1.20.20
# Program: Double For Loop

for i in range(3):
    print("Outer For loop " + str(i))
    for k in range(4):
        print("\tInner for loop " + str(k))



print("\n***************\n")


sum = 0
how_many_numbers = int(input("\nHow many numbers would you like to sum up: "))
print("")

for i in range(how_many_numbers):
    enter_a_number = int(input("Enter a number: "))
    sum = sum + enter_a_number

print("\nSum of your numbers is: " + str(sum))


# Programmer: Jasek Zielaskowski
# Date: 1.7.20
# Program: Average Test Scores

# This program asks users how many tests they wish to average


total = 0
how_many_tests = int(input("\nHow many tests would you like to average: "))
print("")

for i in range(how_many_tests):
    enter_a_score = float(input("Enter a score: "))
    total = total + enter_a_score

Average = total / how_many_tests

print("\nAverage: " + str(round(Average, 2)))


print("\n***************\n")

"""
Programmer: Jasek Zielaskowski
Date: 1.23.20
Program: While Loop nested inside of a For Loop
"""

for i in range(4):
    print("For Loop" + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop " + str(x))
        x = x - 1

# Date: 2.3.20
# Programmer: Jasek Zielaskowski

# Declare Global Variables here

name = input("what is your name:  ")
x = 15


# Create Functions Here

# Greeting Function
def greeting():
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)

# Functions and Local Variable x
def printSomething():
    x = 3
    print(x)
# Functions and Parameters
def printNumber(age): #function name = printNumber with a PARAMETER of age
    print(age)

# Default Parameter Values
def printTwoNumbers(x,y =71):
    print("First Parameter(Number):" + str(x))
    print("Second Parameter(Number):" + str(y))

#Print Sum
def printSum(x,y):
    print(x + y)
#Print Multiple Times
def printMultipleTimes(string, times):
    for i in range (times):
        print(string)

# Call Functions Here
print("\nGreetings Function\n")
greeting()

print("\nPrint Something Function\n")
printSomething()

#print(x)

print("\nPrint Number Function\n")
printNumber(28)
printNumber(38)

print("\nPrint Two Numbers Function\n")
printTwoNumbers(23,78)

print("\nDefault Parameter Values Function\n")
printTwoNumbers(45)
printSum(1,17)

print("\nPrint Multiple Times Function\n")
printMultipleTimes("I love Computer Science", 13)

print("\nThanks for hanging out with me through my fun-ctions")
