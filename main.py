import time
import os
import random
os.system("clear")
print("\x1b[32m")
with open("samples.txt","r") as f:
    samples = f.readlines()
import sys
def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()
while True:
    ans = 3
    while int(ans) > 2 or int(ans) < 0:
        ans = input("input 1 for hacker code\ninput 2 for matrix hacking\n>>")
        os.system("clear")
    if ans == "1":
        ans = 3
        while int(ans) > 2 or int(ans) < 0:
            ans = input("input 1 for hackertyper script\ninput 2 for real code randomly\n>>")
            os.system("clear")
        try:
            while True:
                if ans == "1":
                    with open("hackertyper.txt","r") as file:
                        file = file.readlines()
                        for line in file:
                            for letter in line:
                                time.sleep(0.01)
                                print(letter,end="",flush=True)
                            time.sleep(0.05)
                elif ans == "2":
                    sample = random.choice(samples)
                    for letter in sample:
                        time.sleep(0.01)
                        print(letter,end="",flush=True)
                    time.sleep(0.05)
        except KeyboardInterrupt:
            print("\x1b[0m")
            exit()
    elif ans == "2":
        try:
            while True:
                line=""
                for _ in range(os.get_terminal_size().columns):
                    choice = int(random.random()*2//1)
                    if not _%4 == 0:
                        line+=" "
                    elif _%4 == 0:
                        line += str(choice)
                print(line,end="")
        except KeyboardInterrupt:
            print("\x1b[0m")
            exit()
    elif ans == "" or not ans in ["1","2"]:
        pass