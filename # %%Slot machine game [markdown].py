# %% [markdown]
# We need to get users deposit and then their bet, we can do this by Creating a function called Deposit.

# %%
import random #This can be at the first cell or at the top of the program as well

# %%
#This was added later on to keep the program nice and dynamic, it is a global constant for the project
MAX_LINES = 3
MAX_BETS = 100
MIN_BET = 1
ROWS = 3  
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

# %%
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines


# %% [markdown]
# We need to get sth(a function), that would generate what the outcome of the slot machine will be using the values in the first cell including the symbol count

# %%
def deposit():
    while True:
        amount = input('what would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter number.')

    return amount        

# %%
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
        #print(all_symbols)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            #value = random.choice(all_symbols)
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    #print(columns)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end = ' | ')
            else:
                print(column[row], end = '')

        print()

# %% [markdown]
# Collect bet from user

# %%
def get_number_of_lines():
    while True:
        lines = input('Enter number of lines to bet on(1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Please enter number.')

    return lines        

# %%
def get_bet():
    while True:
        amount = input('what would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BETS:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BETS}.')
        else:
            print('Please enter number.')

    return amount    

# %% [markdown]
# Call the function

# %%
def spin(balance):
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet  = bet * lines

        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}')

        else:
            break
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    print(f'You won on lines:', *winning_lines)
    return winnings - total_bet






def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}' )
        spin_result = input('Press enter to play(q to quit).')
        if spin_result == 'q':
            break
        balance += spin(balance)

    print(f'You left with ${balance}')

main()



# def main():
#     balance = deposit()
#     lines = get_number_of_lines()
#     while True:

    #     bet = get_bet()
    #     total_bet  = bet * lines

    #     if total_bet > balance:
    #         print(f'You do not have enough to bet that amount, your current balance is: ${balance}')

    #     else:
    #         break
    # print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')
    # slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    # print_slot_machine(slots)
    # winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    # print(f'You won ${winnings}.')
#     print(f'You won on lines:', *winning_lines)



# main()

# %% [markdown]
# 

# %%


# %% [markdown]
# **note** - This was initially done at this point in the project, then I moved it as well ass the code below up***
# 
# We need to run the slot machine, so we would need to import some modules, if not installed on system, you can download possibly using ! or % and them import. We would/have set values among our global constants to indicate the number of rows and columns we would have in our slot machine.

# %%
# import random #This can be at the first cell or at the top of the program as well

# %% [markdown]
# **note** - This was initially done at this point in the project, then I moved it as well ass the code below up***
# 
# We need to get sth(a function), that would generate what the outcome of the slot machine will be using the values in the first cell including the symbol count

# %%
# def get_slot_machine_spin(rows, cols, symbols):
#     all_symbols = []
#     for symbol, symbol_count in symbols.items():
#         for _ in range(symbol_count):
#             all_symbols.append(symbol)

#     columns = [[], [], []]
#     for _ in range(cols):
#         column = []
#         current_symbols = all_symbols[:]
#         for _ in range(rows):
#             value = random.choice(all_symbols)
#             current_symbols.remove(value)
#             column.append(value)
        
#         columns.append(column)

#     return columns

# def print_slot_machine(columns):
#     for row in range(len(columns[0])):
#         for i, column in enumerate (columns):
#             if i != len(columns) - 1:
#                 print(column[row], '|')
#             else:
#                 print(column[row])

# %% [markdown]
# Now designing such that if player betting lines are defined, the code is at the top, but it is at this point it was decided.
# 
# This is the code here, but note, I have as well put it at the top
# 

# %%

# def check_winnings(columns, lines, bet, values):
#     winnings = 0
#     winning_lines = []
#     for line in range(lines):
#         symbol = columns[0][line]
#         for column in columns:
#             symbol_to_check = column[line]
#             if symbol != symbol_to_check:
#                 break
#         else:
#             winnings += values[symbol] * bet
#             winning_lines.append(lines + 1)

#     return winnings, winning_lines


# %% [markdown]
# 


