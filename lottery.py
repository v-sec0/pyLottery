#!/bin/python3

# Lottery Simulator 
# Created: 06/29/23


# Imports
from Ticket import Ticket
from time import sleep

# Tickets
conservative = Ticket("Poor Man's Delight", 9.99, 250)
moderate = Ticket("Money Multiplier", 19.99, 500)
risky = Ticket("Uncle Sam Grand Slam", 49.99, 1000)
collection = [conservative, moderate, risky]
cash = 100

# Listing function
def list_tickets():
    print("=" * 58)
    print(f"{'ID'}{'Name': ^15}{'Price': >41}")
    print(f"{'--'}{'----': ^15}{'-----': >41}")
    count = 1
    for item in collection:
        print(f"{str(count) + '.':<6} {item.name: <20} {'$' + str(item.price): >30}")
        count = count + 1
    print("=" * 58)

# Selection function
def selection(cash):
    # Prompting for selection
    choice = 0
    try: 
        while choice != 1 and choice != 2 and choice != 3 and choice != 4:
            choice = int(input("Enter your selection (1|2|3|4)\nOption 4 will exit: "))
            if choice == 1:
                menu(conservative.play(cash))
            elif choice == 2:
                menu(moderate.play(cash))
            elif choice == 3:
                menu(risky.play(cash))
            elif choice == 4:
                print("Exiting.")
                exit()
            else:
                print("Please enter a valid response.")
    except ValueError:
        print("\nError processing choice\n")
    except KeyboardInterrupt:
        print("\n\nQuitter.\n")

        
# Cash check function
def check(cash):
    # Checking your balance
    if cash < conservative.price:
        print("=" * 58)
        print("\nYou went broke!")
        print(f"Your bank account hit: ${cash:.2f}\n")
        print("=" * 50)
        exit()
    print(f"Your total cash is ${cash:.2f}")
    print("You have enough to afford the cheapest card\n")
    print("=" * 50)
    return cash

# Menu function
def menu(cash):
        list_tickets()
        cash_current = selection(check(cash))
# Main funtion
def main():
    # Introduction Banner
    print("=" * 58)
    print("Welcome to the Lottery")
    menu(cash)
main()



    


