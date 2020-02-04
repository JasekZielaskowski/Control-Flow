# Date: 2.3.20
# Greeting Function

# Declare Global Variables here

name = input("what is your name:  ")
x = 15


# Create Functions Here

def greeting():
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)
    print(x)
def printSomething():
    x = 3
    print(x)

#Call Functions Here

greeting()
printSomething()
print(x)