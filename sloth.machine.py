import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS =3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 3,
    "C" :4,
}

SYMBOL_VALUE = {
    "A": 10,
    "B": 5,
    "C": 2,
}

def check_winnings(column, line, bet, value):
    winnings =0
    winning_line = []
    for line3 in range(line):
        symbol = column[0][line3]
        for column1 in column:
            symbol_to_check = column1[line3]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol]* bet
            winning_line.append(line3)

    return winnings, winning_line



def get_slot_machine(row,col,symbol1):
    all_symbol=[]
    for symbol , symbol_count in symbol1.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    
    columns = []
    for _ in range(col):
        column = []
        current_symbol = all_symbol[:]
        for _ in range(row):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
        
    return columns


def print_slot_machine(columns1):
    for row1 in range(len(columns1[0])):
        for i, colum1 in enumerate(columns1):
            if i != len(columns1) -1:
                print(colum1[row1], end=" | ")
            else:
                print(colum1[row1], end="")
        
        print()




def deposit():

    while True:

        amount = input("would you like to enter amount $: ")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break

            else:
                print("amount sholud be greater than 0!")
    
        else:
            print("enter a valid digit number")
    return amount

def number_of_line():
    while True:
        lines = input(f"would you like to enter lines (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines= int(lines)
            if 1 <= lines <= MAX_LINES:
                break

            else:
                print(" lines shold be between under 1-3")
    
        else:
            print("enter a valid number")
    return lines

def bet_amount():
    while True:
        amount = input("would you like to enter Bet-amount $: ")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break

            else:
                print(f"amount sholud be between! {MIN_BET}-{MAX_BET}")
    
        else:
            print("enter a valid digit number")
    return amount

def spin(balance):
    line =  number_of_line()
    while True:
        bet=  bet_amount()
        total_bet = bet * line

        if total_bet > balance:
            print(f"you have not enough amount in wallet your total balance is: {balance}")
        else:
            break
    print(
        f"you bet amount:{bet} on {line} lines and your total bet-amount is: {total_bet}")
    spinn= get_slot_machine(ROWS , COLS, SYMBOL_COUNT)
    print_slot_machine(spinn)
    winning , win_line = check_winnings(spinn, line, bet , SYMBOL_VALUE)
    print(f"you won ${winning}")
    print(f"you won on line", *win_line)
    return winning - total_bet


def main():
    balance8 = deposit()
    while True:
        print(f"current balance is ${balance8}")
        answer = input("Enter to play (q to quit).").lower()
        if answer == "q":
            break
        else:
            balance8 += spin(balance8)

  
main()




    
    





