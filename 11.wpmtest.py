import curses
from curses import wrapper
import time
import random

def main_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("welcome to the speed typing test")
    stdscr.addstr("\npress any key to began!")
    stdscr.refresh()
    stdscr.getkey()

def type_test(stdscr , target , current, wpm=0 , wrong_key=0 ):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"wpm: {wpm}")
    stdscr.addstr(2,0, f"Wrong Keys:  {wrong_key}")
        
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0,i ,char , color)

def file_words():
    with open("storyy.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpr_test(stdscr):
    target_test = "Happy birds chirp loudly, spreading joy through the morning breeze! Small kittens play gently"
    current_test = []
    wpm = 0
    wrong_key = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while True:
        time_elapse = max(time.time() - start_time, 1)
        wpm = round(len(current_test) / (time_elapse/60))/5

        stdscr.clear()
        type_test(stdscr, target_test, current_test, wpm , wrong_key)
        stdscr.refresh()

        if "".join(current_test) == target_test:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        
        if key in ('KEY_BACKSPACE', '\b', '\x7f' ):
            if len(current_test) > 0:
                current_test.pop()
        elif len(current_test) < len(target_test):
            if key != target_test[len(current_test)]:
                wrong_key += 1
            current_test.append(key)

            if len(current_test) == len(target_test) and "".join(current_test) != target_test:
                target_test = file_words()
                current_test =[]
                start_time = time.time()





def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED ,curses.COLOR_BLACK)

    main_screen(stdscr)
    while True:
        wpr_test(stdscr)

        stdscr.addstr(2,0, "you complete your task! press any key to continue....")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper (main)
