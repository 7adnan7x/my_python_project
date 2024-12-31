from playsound import playsound
import time
CLEAR = "\033[2J"
CLEAR_RETURN = "\033[H"
print(CLEAR)

def alaram4(seconds):
    
    time_frac= 0
    print(CLEAR)
    while time_frac < seconds:
        time.sleep(1)
        time_frac += 1

        time_left = seconds - time_frac
        minute_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_RETURN}alaram will sound in  {minute_left:02d}:{seconds_left:02d}")

    playsound("alaram9.mp3")

minute = int(input("minute you want to set alaram: "))
second = int(input("second you want to set alaram: "))
total_Time = minute* 60 + second

adn = alaram4( total_Time)


