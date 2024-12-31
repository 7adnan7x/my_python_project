import random
import time

min_number= 1
max_number = 8
operator = ["+","-","*"]
tot_question = 4

def Result1():
    left = random.randint(min_number, max_number)
    right = random.randint(min_number , max_number)
    ope = random.choice(operator)
    exp = str(left)+" " + ope + " " + str(right) 
    answer= eval(exp)
    return exp , answer


wrong= 0
input("press inter to start")
print("-------------") 

start_time = time.time()

for i in range(tot_question):
    exp , answer = Result1()
    while True:
        guess = input("problem # "+ str(i + 1)+ ": "+ exp + "= ")
        if guess == str(answer):
            print("correct")
            break
        else:
            print("incorrect right answer is", answer)
            wrong += 1
            break


end_time = time.time()
total_time = round(end_time - start_time, 2)
print("------------")
print("nice work", total_time)
print("total wrong answer is", wrong)





