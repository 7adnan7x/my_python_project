import turtle
import time
import random
WIDTH , HEIGHT = 500, 500
COLORS = ['red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'brown','cyan']



def number_of_racer():
    

    while True:
        answer= input("enter the number of turtle you want to play: (2-10): ")
        if answer.isdigit():
            answer = int(answer)
        else:
            print("the number shoud be a valid number!")
            continue
            
    
    
        if 2 <= answer <= 10:
            
            return answer
        else:
            print("number should be between 2 to 10")

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x,y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors [turtles.index(racer)]
        

    



def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):

        racer= turtle.Turtle()
        racer.speed(1)
        racer.penup()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.setpos(-WIDTH //2  + (i + 1)* spacingx , -HEIGHT // 2 +20)
        racer.pendown()
        turtles.append(racer)

    return turtles 

            
def init_turtle():
    screen = turtle.Screen()
    screen.setup( WIDTH, HEIGHT )
    screen.title("TURTLE RACE")
            
racers = number_of_racer()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[: racers]
winner = race(colors)
print("the winner color is", winner)
time.sleep(5)

