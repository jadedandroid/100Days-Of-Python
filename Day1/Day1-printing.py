print("Hello World!")
# basic printing👇
# print("Day 1 - Python Print Function")
# print("The function is Declared like this:")
# print("print('what to print')")

# multi line printing
# print("Hello World! \nHelloWorld\nHelloWorld")

# string cancatenation 
# print("Hello" + " " + "Jade" + " How are you")

# Input Function
# input("what is your name ")


# nested input function
# print("Hello" + input('What is your name ')+ "!")
#  print the length of the inputed string
print( len( input("what is your name? ") ) )

# save the input to a variable 
name = input("what is your name? ")
length = len(name)
print(length)


################# Band name Generator ############
#1. Create a greeting for your program.
print("Welcome to the Band name generator")
#2. Ask the user for the city that they grew up in.
city = input("what city did you grow up in? ")

#3. Ask the user for the name of a pet.
pet = input("did you have or own any pets? " )

#4. Combine the name of their city and pet and show them their band name.
print("your band name is "+ city + pet)
