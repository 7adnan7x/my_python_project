import random
def roll():
    min_value= 1
    max_value= 6

    roll= random.randint(min_value ,max_value)
    return roll

while True:
    players= input("enter the number between (2-4): ")
    if players.isdigit():
        players= int(players)
        if (2<= players <=4):
            break
        else:
            print("number shoud be between 2-4")

    else:
        print("invalid number try again")

max_score= 50
player_score =[0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print("player number",player_idx +1,"turn has started")
        print("your total score is: ",player_score[player_idx])
        current_score = 0

        while True:
            input_= input("would you like to roll (y)")
            if input_.lower() != "y":
                break

            value= roll()
            if value == 1:
                print("you roll 1! here your Turn is done")
                current_score = 0
                break

            else:
                current_score += value
                print("you rolled a: ", value)
            print('your score is:',current_score)

        player_score[player_idx]+= current_score
        print("player number is:", player_idx+1,"your total score is: ",player_score[player_idx])


maxscore= max(player_score)
win_idx= player_score.index(maxscore)
print("player number:",win_idx +1,"is the winner with the score of",maxscore)



            




        





