import random
CODE_LENGTH = 4
COLOR = ["R", "G", "Y", "B", "W","O"]
TRIES = 20
def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLOR)
        code.append(color)
    return code


def guess_code():
    while True:
        guess = input("guess :").upper().split(' ')
        if len(guess) != CODE_LENGTH:
            print(f"guess under {CODE_LENGTH} color")
            continue

        for color in guess:
            if color not in COLOR:
                print(f"invaild! color{color}")
                break
        
        else:
            break

    return guess

def check_code(guess, generate_code):
    color_counts ={}
    correct_pos = 0
    incorrect_pos = 0

    for color in generate_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    for guess_color , real_color in zip(guess, generate_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    for guess_color , real_color in zip(guess , generate_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
    
    return correct_pos , incorrect_pos

       

def game():
    print(f"hey! welocome to game you have{TRIES}")
    print("the valid color are", *COLOR)

    code = generate_code()
    for attempt in range(1, TRIES +1):
        guess = guess_code()
        correct_pos , incorrect_pos = check_code(guess , code)
         
        if correct_pos == CODE_LENGTH:
            print(f"you gussed the code in {attempt} tries")
            break
        print(f"correct_position: {correct_pos}|incorrect_position: {incorrect_pos}")

    
    else:
        print("you run out correct colore is: "*code)
if __name__== "__main__":
    game()
        