import random

jackpot = 500
testItem = False
rounds = 0

while not testItem:
    
    print(f'\nThe highest amount to win is ${jackpot}')

    # Getting potential earnings index and adjusted probability index
    winning_index = random.randint(0,100) / 100
    losing_index = random.randint(0,100) / 100

    # Printing information
    print(f'Win index: {winning_index}')
    print(f'Lose index: {losing_index}')

    # Testing to see if values match
    if winning_index != losing_index:
        print("Values do not match")
        rounds = rounds + 1
    else:
        print(f'It took {rounds} rounds to get a matching value')
        add_win_index = random.randint(0,100)
        add_loss_index = random.randint(0,100)

        # Printing information
        print(f'Add Win index: {add_win_index}')
        print(f'Add Lose index: {add_loss_index}')

        if add_loss_index == add_win_index:
            testItem = True
            print(f'It took {rounds} rounds to get a winning pair')
        else:
            rounds = rounds + 1

