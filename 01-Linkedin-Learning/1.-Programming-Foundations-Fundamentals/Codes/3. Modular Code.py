# Modular Code

'''
Instead of repeating the code a hundred times
you can write once 
and print it in the amount you want
'''

print("~~~ The Shimmy ~~~")

def shimmy():
    print("Take one step to the right and stomp.")
    print("Take one step to the left and stomp.")
    print("Shake those hips!")

shimmy()
shimmy()
shimmy()

'''
Here we used the terms in order to make the user choose
'''

def wash_car(amount_paid):
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

    else:
        print("Not Found")

wash_car(12) 

# Returning values from Functions

def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100, 80)

if (balance <= 50):
    print("We need to make a deposit")
else:
    print("Nothing to see here!")

