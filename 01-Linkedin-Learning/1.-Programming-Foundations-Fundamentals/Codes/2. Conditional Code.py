# Conditional Code

'''
This code asks you about your age
if you are older than 13
if the condition is found and the first command is executed
if your age is younger 
the second code is executed
'''

name = input("Hi, what's your name? ")
age = int(input("How old are you? "))

if (age < 13):
    print("You're too young to register", name)

else:
    print("Feel free to join", name)

'''
This code asks you 
if you enjoying the corse or not 
it gives you the result of your choice
'''
print("Hi!")

name = input("What's your name? ")
print("It's nice to meet you,", name)

answer = input("Are you enjoying the course? ")

if answer == "Yes":
    print("That's good to hear!")

else:
    print("Oh no! That makes me sad!")

print("Final statement")

# Simple Condition

plant = "Cacti"

if plant == "Cacti":
    print(plant, "don't need a lot of water")
else:
    print(plant, "love water")

print("Thanks!")


