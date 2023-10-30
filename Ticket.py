# Ticket Object

# Imports
import random

class Ticket:
    
    def __init__ (self, name, price, jackpot) -> None:
        self.name = name
        self.price = price
        self.jackpot = jackpot
           

    def play(self, cash):
        
        # Repeating selection 
        print(f"\n{self.name} has been selected.")

        # Asking for amount without over shooting
        clear = False
        while clear == False:
            try:
                amount = int(input(f"Enter the amount of {self.name} ticket's you would like: "))
                if ((amount*self.price) > cash):
                    print("You can't afford this.")
                else:
                    clear = True
            except ValueError:
                print("\nEnter a number\n")
            except KeyboardInterrupt:
                print("\n\nQuitting\n")
                exit()
        paid = (amount*self.price)
        cost = cash - paid
        print(f"{amount} tickets have been selected, costing ${paid} and leaving ${cost:.2f} behind.")
       

        # Rolling the odds
        print("=" * 50)
        print("Game Time!")
        print("=" * 50)
        earnings = 0
        
        # Initializing the loop 
        for ticket_num in range(amount):
            
            # Creating win-lose indexes
            winning_index = random.randint(0,100)
            losing_index = random.randint(0,100)

            # Establishing brackets
            win_brackets = ['High Gains', 'Mid Gains', 'Low Gains']
            win_weight = [10, 20, 70]
            lose_bracket = ['High Loss', 'Mid Loss', 'Some Loss', 'Low Loss']
            lose_weight = [80, 15, 7, 3]

            # Figuring out the gains/losses
            gains_group = random.choices(win_brackets, weights=win_weight, k=1)[0]
            losses_group = random.choices(lose_bracket, weights=lose_weight, k=1)[0]
            

            # Making sure indexes don't match and result in lottery chance
            if winning_index != losing_index:
                # Working with win bracket
                if gains_group == 'High Gains':
                    max_gains = (self.jackpot * .75)
                    min_gains = (self.jackpot * .50)
                elif gains_group == "Mid Gains":
                    max_gains = (self.jackpot * .50)
                    min_gains = (self.jackpot * .25)
                else:
                    max_gains = (self.jackpot * .25)
                    min_gains = (self.jackpot * 0)
            else:
                # Working with win bracket
                if gains_group == 'High Gains':
                    max_gains = (self.jackpot * 1)
                    min_gains = (self.jackpot * .75)
                elif gains_group == "Mid Gains":
                    max_gains = (self.jackpot * .75)
                    min_gains = (self.jackpot * .25)
                else:
                    max_gains = (self.jackpot * .25)
                    min_gains = (self.jackpot * 0)

            # Working with lose bracket
            if losses_group == "High Loss":
                max_loss = 100
                min_loss = 75
            elif losses_group == "Mid Loss":
                max_loss = 74
                min_loss = 50
            elif losses_group == "Some Loss":
                max_loss = 49
                min_loss = 25
            else:
                max_loss = 24
                min_loss = 0

            # Finding the value won
            amount_won = random.uniform(min_gains, max_gains)
            losing_percent = random.randint(min_loss, max_loss)

            true_amount = amount_won - (amount_won * (losing_percent/100))

            # Making sure negatives aren't given
            if true_amount < 0:
                true_amount = 0
            
            # Printing the scratch off results
            print(f'\n Scratching ticket #{ticket_num + 1}\n You won ${true_amount:.2f}\n')
            print(f'Debugging: Amount Won ${amount_won:.2f} | Losing Percent {losing_percent:.2f}%')
            earnings =+true_amount

        # Printing final earnings
        true_earnings = earnings - paid
        print(f'Total earned: ${true_earnings:.2f}')
        print(f'Previous balance: ${paid + cost:.2f}')
        print("=" * 58)
        print("#" * 58)
        

        # Return cash
        return (cost + earnings)

        
        
        
